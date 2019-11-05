import glob, csv, os, re
from model import CreditCardRecord

class CSVReader():
    def __init__(self):
        self.record_list = []

    def process_csv_data_by_folder(self, folder_path):
        for filename in glob.glob(os.path.join(folder_path, '*.csv')):
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        year = row[0].split('-')[0]
                        month = row[0].split('-')[1]
                        day = row[0].split('-')[2]
                        category = row[1]
                        store = row[2]
                        amount = row[3]
                        installment_amount = None
                        installment = None
                        match = re.search('\d+/\d+', store)
                        # print(match.group())
                        if match:
                            installment_amount = match.group().split('/')[1]
                            installment = match.group().split('/')[0]
                        record = CreditCardRecord(year=year, month=month, day=day, amount=amount, category=category, store=store, installment_amount=installment_amount, installment=installment)
                        self.record_list.append(record.toJSON())
                        line_count += 1
        return self.record_list

    def process_csv_data_by_file(self, file_path):
        #TODO
        return self.record_list

    def get_record_list(self):
        return self.record_list



        '^[^0-9]\\[^0-9]$'