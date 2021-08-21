# coding: utf-8
import json, re
from decimal import Decimal
from datetime import datetime
from credit_card.models import CreditCardRecord

class RecordTranslator():

    def valid_fields(self, row_fields):
        required_fields = [0, 2, 3]
        return len(row_fields) == 4 and all([row_fields[i] != '' for i in required_fields])

    def translate_csv_row_to_record(self, csv_row, user, file_name):
        fields = csv_row.decode().replace('"', "").replace("\n", "").split(',')
        if self.valid_fields(fields):
            record = {}
            record['file'] = file_name
            record['date'] = datetime.strptime(fields[0], "%Y-%m-%d").date()
            record['category'] = fields[1]
            record['amount'] = fields[3]
            match = re.search('\d+/\d+', fields[2])
            if match:
                instalment_payment = match.group().split('/')[0]
                record['installment_total'] = int(match.group().split('/')[1])
                record['installment_payment'] = int(instalment_payment)
                record['store'] = fields[2].split(instalment_payment)[0].strip()
            else:
                record['installment_total'] = 0
                record['installment_payment'] = 0
                record['store'] = fields[2]
            record['user'] = user.id
            return record
        return None