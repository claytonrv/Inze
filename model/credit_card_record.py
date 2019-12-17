# coding: utf-8
import json

class CreditCardRecord:
    def __init__(self, year, month, day, amount, category, store, installment_amount, installment):
        self.year=year
        self.month=month
        self.day=day
        self.amount=float(amount) if (amount is not None and amount != "") else 0.0
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

    def get_installment_amount(self):
        return self.installment_amount

    def set_installment_amount(self, installment_amount):
        self.installment_amount = installment_amount

    def get_installment(self):
        return self.installment

    def set_installment(self, installment):
        self.installment = installment

    def to_string(self):
        return "Ano: "+self.year +" | Mês: "+ self.month +" | Dia: "+ self.day +" | Montante: "+ self.amount +" | Categoria: "+ self.category +" | Loja:"+self.store + " | Parcelamento: "+self.installment_amount + " | Parcelas pagas: "+self.installment 

    def to_dict(self):
        if self.year is not None and self.month is not None and self.day is not None and self.category is not None and self.store is not None:
            return {
                'year': self.year,
                'month': self.month,
                'day': self.day,
                'amount': self.amount,
                'category': self.category,
                'store': self.store,
                'installment_amount': self.installment_amount,
                'installment': self.installment
            }
        else:
            return None