# coding: utf-8
import glob, csv, os
from model import CreditCardRecord
from translation import RecordTranslator

class CSVReader():
    def __init__(self):
        self.record_list = []
        self.record_translator = RecordTranslator()

    def process_csv_data_by_folder(self, folder_path):
        for filename in glob.glob(os.path.join(folder_path, '*.csv')):
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        record = self.record_translator.translate_csv_row_to_record(row)
                        self.record_list.append(self.record_translator.translate_record_to_json(record))
                        line_count += 1
        return self.record_list

    def process_csv_data_by_file(self, file_path):
        #TODO
        return self.record_list

    def get_record_list(self):
        return self.record_list
