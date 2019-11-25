# coding: utf-8
import json, re
from model import CreditCardRecord

class RecordTranslator():

    def translate_record_list_to_json_list(self, record_list):
        json = "["
        for record in record_list:
            json += record+","
        json = json[:-1]
        json += "]"
        return json

    def translate_record_to_json(self, record):
        return json.dumps(record, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

    def translate_csv_row_to_record(self, csv_row):
        year = csv_row[0].split('-')[0]
        month = csv_row[0].split('-')[1]
        day = csv_row[0].split('-')[2]
        category = csv_row[1]
        store = csv_row[2]
        amount = csv_row[3]
        installment_amount = None
        installment = None
        match = re.search('\d+/\d+', store)
        if match:
            installment_amount = match.group().split('/')[1]
            installment = match.group().split('/')[0]
        record = CreditCardRecord(year=year, month=month, day=day, amount=amount, category=category, store=store, installment_amount=installment_amount, installment=installment)