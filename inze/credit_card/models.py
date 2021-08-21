from django.db import models
from django.contrib.auth.models import User

class CreditCardRecord(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=120)
    store = models.CharField(max_length=120)
    installment_total = models.IntegerField()
    installment_payment = models.IntegerField()
    file= models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="credit_card_records")


class CreditCardBillFile(models.Model):
    file = models.FileField(upload_to=None, max_length=100)
    def __str__(self):
        return self.file.name