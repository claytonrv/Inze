# coding: utf-8
import glob, csv, os
from model import CreditCardRecord
from translation import RecordTranslator

class CSVHandler():
    def __init__(self):
        self.list_of_record_json = []
        self.record_translator = RecordTranslator()

    def transform_csv_files_into_json_by_folder(self, folder_path):
        for filename in glob.glob(os.path.join(folder_path, '*.csv')):
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        json_record = self.transform_csv_row_into_json(row)
                        self.list_of_record_json.append(json_record)
                        line_count += 1
        return self.list_of_record_json

    def transform_csv_row_into_json(self, row):
        record = self.record_translator.translate_csv_row_to_record(row)
        return self.record_translator.translate_record_to_json(record)

    def get_list_of_record_list(self):
        return self.list_of_record_json
