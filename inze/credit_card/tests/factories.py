import random
import factory

from decimal import Decimal

from datetime import date

from django.contrib.auth.models import User

from credit_card.models import CreditCardRecord

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = "jeff.belson"
    first_name = "Jeff"
    last_name = "Sumo Belson"
    email = "jeff.belson@example.com"


class CreditCardRecordFactory(factory.Factory):
    class Meta:
        model = CreditCardRecord
    
    date = date(2015, 7, 31)
    amount =  Decimal(random.randrange(1, 257))/100
    category = "saúde"
    store = factory.Faker("company")
    installment_total = 2
    installment_payment = 1
    file = "nubank-2015-08.csv"
    user = factory.SubFactory(UserFactory)