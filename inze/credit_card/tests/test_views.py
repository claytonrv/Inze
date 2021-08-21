import pytest

from django.urls import reverse
from django.test import Client

from credit_card.tests.factories import CreditCardRecordFactory

class TestCreditCardRecordViewset:

    @pytest.fixture
    def client(self):
        return Client()

    @pytest.fixture
    def credit_card_records(self):
        return CreditCardRecordFactory.create_batch(3)

    
    @pytest.mark.usefixture('credit_card_records')
    def test_access_the_list(self, client):

        response = client.get(reverse('rest_framework'))

        assert response.status_code == 200