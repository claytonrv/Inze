# coding: utf-8
import json, re
from decimal import Decimal
from datetime import datetime
from credit_card.models import CreditCardRecord

class RecordTranslator():

    def translate_record_to_json(self, record):
        return json.dumps(record, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

    def translate_csv_row_to_record(self, csv_row, user, file_name):
        fields = csv_row.decode().replace('"', "").replace("\n", "").split(',')
        record = {}
        record['file'] = file_name
        record['date'] = datetime.strptime(fields[0], "%Y-%m-%d").date()
        record['category'] = fields[1]
        record['store'] = fields[2]
        record['amount'] = fields[3]
        match = re.search('\d+/\d+', record['store'])
        if match:
            record['installment_total'] = int(match.group().split('/')[1])
            record['installment_payment'] = int(match.group().split('/')[0])
        else:
            record['installment_total'] = 0
            record['installment_payment'] = 0
        record['user'] = user.id
        return record