import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from django.contrib.auth.models import User

from credit_card.tests.factories import CreditCardRecordFactory
from credit_card.models import CreditCardRecord


@pytest.mark.django_db
class TestCreditCardRecordViewset:
    @pytest.fixture
    def user(self):
        return User.objects.create_user(
            username="user", email="user@foo.com", password="top_secret"
        )

    @pytest.fixture
    def token(self, user):
        client = APIClient()
        payload = {"username": user.username, "password": "top_secret"}
        response = client.post(reverse("token"), payload)
        return response.data["token"]

    @pytest.fixture
    def client(self):
        return APIClient()

    @pytest.fixture
    def credit_card_records(self):
        return CreditCardRecordFactory.create_batch(3)

    def test_acces_list_without_auth_returns_401_unauthorized(self, client):
        response = client.get(reverse("cc-records"))
        assert response.status_code == 401

    @pytest.mark.usefixtures("credit_card_records")
    def test_access_the_list(self, client, token):
        client.credentials(HTTP_AUTHORIZATION="Token " + token)
        response = client.get(reverse("cc-records"))

        assert response.status_code == 200

    @pytest.mark.usefixtures("credit_card_records")
    def test_get_all_record_lines(self, client, token):
        CreditCardRecordFactory.create_batch(2, file="2015-09.csv")
        client.credentials(HTTP_AUTHORIZATION="Token " + token)
        response = client.get(reverse("cc-records"))
        records = response.data
        assert len(records) == 5

    @pytest.mark.usefixtures("credit_card_records")
    def test_get_record_lines_from_file(self, client, token):
        file_name = "nubank-2015-08.csv"

        client.credentials(HTTP_AUTHORIZATION="Token " + token)
        response = client.get(reverse("cc-records"), {"file_name": file_name})

        assert response.status_code == 200
        records = response.data
        assert len(records) == 3
        for record in records:
            assert record["date"] == "2015-07-31"
            assert record["amount"] is not None
            assert record["category"] == "saúde"
            assert record["store"] is not None
            assert record["installment_total"] == 2
            assert record["installment_payment"] == 1
            assert "user_" in record["user"]
            assert record["file"] == "nubank-2015-08.csv"

    @pytest.mark.usefixtures("credit_card_records")
    def test_get_record_lines_from_invalid_file(self, client, token):
        file_name = "nubank-2022-03.csv"

        client.credentials(HTTP_AUTHORIZATION="Token " + token)
        response = client.get(reverse("cc-records"), {"file_name": file_name})
        assert response.status_code == 200
        records = response.data
        assert len(records) == 0
