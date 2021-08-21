import pytest
from datetime import datetime

from credit_card.tests.factories import CreditCardRecordFactory

from credit_card.serializers import CreditCardRecordSerializer, CreditCardRecordListSerializer

class TestCreditCardRecordSerializer:
    @pytest.fixture
    def csv_content(self, user, csv_filename):
        return {
            'date': datetime.strptime('2015-07-27', "%Y-%m-%d").date(),
            'amount': '14.05',
            'category': "",
            'store': "IOF de Tjmaxx $0142 Norwell Ma",
            'installment_total': 0,
            'installment_payment': 0,
            'file': csv_filename,
            'user': user.id,
        }

    @pytest.mark.django_db
    def test_it_validates_data(self, csv_content):
        serializer = CreditCardRecordSerializer(data=csv_content)
        serializer.is_valid(raise_exception=True)

class TestCreditCardRecordListSerializer:

    @pytest.fixture
    def credit_card_record(self):
        return CreditCardRecordFactory()

    def test_it_return_correct_fields(self, credit_card_record):
        serializer = CreditCardRecordListSerializer(credit_card_record)
        assert serializer.data['user'] == 'jeff.belson'
        assert serializer.data['amount'] == str(credit_card_record.amount)
        assert serializer.data['category'] == 'saúde'
        assert serializer.data['store'] == credit_card_record.store
        assert serializer.data['installment_total'] == 2
        assert serializer.data['installment_payment'] == 1
        assert serializer.data['file'] == "nubank-2015-08.csv"