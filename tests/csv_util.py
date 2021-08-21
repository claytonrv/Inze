# coding: utf-8
class CSVUtil:
    def __init__(self):
        self.csv_row=None
        self.json_row=None
        self.csv_file_path=None

    def init_valid_csv_row(self):
        return ['2019-09-19', 'outros', 'Paypal *Uber', '15.9']

    def init_valid_csv_json(self):
        return ('{\n'
                '    "amount": 15.9,\n' 
                '    "category": "outros",\n'
                '    "day": "19",\n' 
                '    "installment": null,\n' 
                '    "installment_amount": null,\n' 
                '    "month": "09",\n' 
                '    "store": "Paypal *Uber",\n'
                '    "year": "2019"\n'
            '}')

    def init_invalid_csv_row(self):
        return [None, None, None, None]

    def init_invalid_csv_json(self):
        return ('{\n'
                '    "amount": 0.0,\n' 
                '    "category": null,\n'
                '    "day": null,\n' 
                '    "installment": null,\n' 
                '    "installment_amount": null,\n' 
                '    "month": null,\n' 
                '    "store": null,\n'
                '    "year": null\n'
            '}')

    def init_empty_csv_row(self):
        return ['', '', ' ', '']
    
    def init_empty_csv_json(self):
        return ('{\n'
                '    "amount": 0.0,\n' 
                '    "category": null,\n'
                '    "day": null,\n' 
                '    "installment": null,\n' 
                '    "installment_amount": null,\n' 
                '    "month": null,\n' 
                '    "store": null,\n'
                '    "year": null\n'
            '}')
    
    def init_list_csv_json(self):
        return [('{\n'
                '    "amount": 108.49,\n' 
                '    "category": "eletrônicos",\n'
                '    "day": "03",\n' 
                '    "installment": "2",\n' 
                '    "installment_amount": "10",\n' 
                '    "month": "09",\n' 
                '    "store": "Amazon-Marketplace 2/10",\n'
                '    "year": "2019"\n'
                '}'),
                ('{\n'
                '    "amount": 27.9,\n' 
                '    "category": "restaurante",\n'
                '    "day": "03",\n' 
                '    "installment": null,\n' 
                '    "installment_amount": null,\n' 
                '    "month": "09",\n' 
                '    "store": "Burger King",\n'
                '    "year": "2019"\n'
                '}'),
                ('{\n'
                '    "amount": 26.9,\n' 
                '    "category": "outros",\n'
                '    "day": "14",\n' 
                '    "installment": null,\n' 
                '    "installment_amount": null,\n' 
                '    "month": "09",\n' 
                '    "store": "Ebanx *Spotify",\n'
                '    "year": "2019"\n'
                '}'),
                ('{\n'
                '    "amount": 15.9,\n' 
                '    "category": "outros",\n'
                '    "day": "19",\n' 
                '    "installment": null,\n' 
                '    "installment_amount": null,\n' 
                '    "month": "09",\n' 
                '    "store": "Paypal *Uber",\n'
                '    "year": "2019"\n'
                '}')]

    def init_valid_csv_file_path(self):
        return "tests/resource/valid/"

    def init_empty_csv_file_path(self):
        return "tests/resource/empty/"