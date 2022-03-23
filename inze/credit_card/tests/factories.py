import random
import factory

from decimal import Decimal

from datetime import date

from django.contrib.auth.models import User

from credit_card.models import CreditCardRecord


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_%d" % n)
    first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    last_name = factory.Sequence(lambda n: "Agent %03d" % n)
    email = factory.LazyAttribute(
        lambda a: "{}.{}@example.com".format(a.first_name, a.last_name).lower()
    )
    password = "my_password"


class CreditCardRecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CreditCardRecord

    date = date(2015, 7, 31)
    amount = Decimal(random.randrange(1, 257)) / 100
    category = "saúde"
    store = factory.Faker("company")
    installment_total = 2
    installment_payment = 1
    file = "nubank-2015-08.csv"
    user = factory.SubFactory(UserFactory)
