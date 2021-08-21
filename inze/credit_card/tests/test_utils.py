import pytest
from datetime import datetime
from decimal import Decimal
from credit_card.utils import RecordTranslator
from credit_card.models import CreditCardRecord

@pytest.fixture
def csv_row():
    return b'2015-07-27,,IOF de "Tjmaxx $0142 Norwell Ma",14.05\n'

@pytest.fixture
def invalid_csv_row():
    return b',,,'

@pytest.fixture
def translator():
    return RecordTranslator()

@pytest.mark.django_db
def test_it_translate_csv_row_to_record(csv_row, translator, user, csv_filename):
    expected_record = {}
    expected_record['date'] = datetime.strptime('2015-07-27', "%Y-%m-%d").date()
    expected_record['amount'] = '14.05'
    expected_record['category'] = ""
    expected_record['store'] = "IOF de Tjmaxx $0142 Norwell Ma"
    expected_record['installment_total'] = 0
    expected_record['installment_payment'] = 0
    expected_record['file'] = csv_filename
    expected_record['user'] = user.id
    translated_row = translator.translate_csv_row_to_record(csv_row, user, csv_filename)
    assert translated_row == expected_record

@pytest.mark.django_db
def test_it_does_not_fail_on_invalid_csv_row(invalid_csv_row, translator, user, csv_filename):
    expected_record = None
    translated_row = translator.translate_csv_row_to_record(invalid_csv_row, user, csv_filename)
    assert translated_row == expected_record

@pytest.mark.django_db
def test_it_get_installment_from_store_field(translator, user, csv_filename):
    csv_row = b'2015-07-28,lazer,Minecraft Net 1/3,93.25\n'
    expected_record = {}
    expected_record['date'] = datetime.strptime('2015-07-28', "%Y-%m-%d").date()
    expected_record['amount'] = '93.25'
    expected_record['category'] = "lazer"
    expected_record['store'] = "Minecraft Net"
    expected_record['installment_total'] = 3
    expected_record['installment_payment'] = 1
    expected_record['file'] = csv_filename
    expected_record['user'] = user.id
    translated_row = translator.translate_csv_row_to_record(csv_row, user, csv_filename)
    assert translated_row == expected_record