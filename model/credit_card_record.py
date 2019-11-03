import json

class CreditCardRecord:
    def __init__(self, year, month, day, amount, category, store, installment_amount, installment):
        self.year=year
        self.month=month
        self.day=day
        self.amount=amount
        self.category=category
        self.store=store
        self.installment_amount=installment_amount
        self.installment=installment

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_amount(self):
        return self.amount
    
    def get_category(self):
        return self.category

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month=month

    def set_day(self, day):
        self.day=day

    def set_amount(self, amount):
        self.amount=amount

    def set_category(self, category):
        self.category=category
    
    def get_store(self):
        return self.store

    def set_store(self, store):
        self.store = store

    def to_string(self):
        return "Ano: "+self.year +" | Mês: "+ self.month +" | Dia: "+ self.day +" | Montante: "+ self.amount +" | Categoria: "+ self.category +" | Loja:"+self.store

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)