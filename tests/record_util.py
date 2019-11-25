import sys, json
sys.path.append('../')
from model import CreditCardRecord

class RecordUtil():
    def __init__(self):
        self.record = None
        self.record_list = None
        self.json = None
        self.json_list = None

    def initValidRecord(self):
        return CreditCardRecord(year="2019", month="09", day="03", amount="271.24", category="eletrônicos", store="Havan Loja de Deptos", installment_amount="3", installment="2")

    def initValidRecordList(self):
        record1 = CreditCardRecord(year="2019", month="11", day="09", amount="271.24", category="eletrônicos", store="Havan Loja de Deptos", installment_amount="3", installment="2")
        record2 = CreditCardRecord(year="2019", month="11", day="10", amount="72.40", category="alimentação", store="Bistek Supermercados", installment_amount=None, installment=None)
        record3 = CreditCardRecord(year="2019", month="11", day="11", amount="21.15", category="saúde", store="Preço popular farmácias", installment_amount="2", installment="1")
        return [record1, record2, record3]

    def initInvalidRecord(self):
        return CreditCardRecord(year=None, month=None, day=None, amount=None, category=None, store=None, installment_amount=None, installment=None)

    def initInvalidRecordList(self):
        record1 = CreditCardRecord(year=None, month=None, day=None, amount=None, category=None, store=None, installment_amount=None, installment=None)
        record2 = CreditCardRecord(year=None, month=None, day=None, amount=None, category=None, store=None, installment_amount=None, installment=None)
        record3 = CreditCardRecord(year=None, month=None, day=None, amount=None, category=None, store=None, installment_amount=None, installment=None)
        return [record1, record2, record3]

    def initEmptyRecord(self):
        return CreditCardRecord(year="", month="", day="", amount="", category="", store="", installment_amount="", installment="")

    def initEmptyRecordList(self):
        record1 = CreditCardRecord(year="", month="", day="", amount="", category="", store="", installment_amount="", installment="")
        record2 = CreditCardRecord(year="", month="", day="", amount="", category="", store="", installment_amount="", installment="")
        record3 = CreditCardRecord(year="", month="", day="", amount="", category="", store="", installment_amount="", installment="")
        return [record1, record2, record3]

    def initRecordJson(self):
        return ('{\n'
                '    "amount": "271.24",\n' 
                '    "category": "eletrônicos",\n'
                '    "day": "03",\n' 
                '    "installment": "2",\n' 
                '    "installment_amount": "3",\n' 
                '    "month": "09",\n' 
                '    "store": "Havan Loja de Deptos",\n'
                '    "year": "2019"\n'
            '}')

    def initRecordJsonList(self):
        json_list = ('[{\n'
                '    "amount": "271.24",\n' 
                '    "category": "eletrônicos",\n'
                '    "day": "09",\n' 
                '    "installment": "2",\n' 
                '    "installment_amount": "3",\n' 
                '    "month": "11",\n' 
                '    "store": "Havan Loja de Deptos",\n'
                '    "year": "2019"\n'
            '},{\n'
                '    "amount": "72.40",\n' 
                '    "category": "alimentação",\n' 
                '    "day": "10",\n' 
                '    "installment": null,\n' 
                '    "installment_amount": null,\n' 
                '    "month": "11",\n' 
                '    "store": "Bistek Supermercados",\n' 
                '    "year": "2019"\n'
            '},{\n'
                '    "amount": "21.15",\n' 
                '    "category": "saúde",\n' 
                '    "day": "11",\n' 
                '    "installment": "1",\n' 
                '    "installment_amount": "2",\n' 
                '    "month": "11",\n' 
                '    "store": "Preço popular farmácias",\n' 
                '    "year": "2019"\n'
            '}]')
        return json_list

    def initInvalidRecordJson(self):
        return json.dumps({
            "amount": None,
            "category": None,
            "day": None,
            "installment": None,
            "installment_amount": None,
            "month": None,
            "store": None,
            "year": None
        }, indent=4)
    
    def initInvalidRecordJsonList(self):
        return json.dumps([
            {
                "amount": None,
                "category": None,
                "day": None,
                "installment": None,
                "installment_amount": None,
                "month": None,
                "store": None,
                "year": None
            },
            {
                "amount": None,
                "category": None,
                "day": None,
                "installment": None,
                "installment_amount": None,
                "month": None,
                "store": None,
                "year": None
            },
            {
                "amount": None,
                "category": None,
                "day": None,
                "installment": None,
                "installment_amount": None,
                "month": None,
                "store": None,
                "year": None
            }
        ], indent=4)

    def initEmptyRecordJson(self):
        return json.dumps({
            "amount": "",
            "category": "",
            "day": "",
            "installment": "",
            "installment_amount": "",
            "month": "",
            "store": "",
            "year": ""
        }, indent=4)

    def initEmptyRecordJsonList(self):
        return json.dumps([
            {
            "amount": "",
            "category": "",
            "day": "",
            "installment": "",
            "installment_amount": "",
            "month": "",
            "store": "",
            "year": ""
            },
            {
            "amount": "",
            "category": "",
            "day": "",
            "installment": "",
            "installment_amount": "",
            "month": "",
            "store": "",
            "year": ""
            },
            {
            "amount": "",
            "category": "",
            "day": "",
            "installment": "",
            "installment_amount": "",
            "month": "",
            "store": "",
            "year": ""
            }
        ], indent=4)