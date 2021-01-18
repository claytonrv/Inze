from django.contrib import admin

from credit_card.models import CreditCardRecord

# Register your models here.
class CreditCardRecordAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "amount",
        "category",
        "store",
        "installment_total",
        "installment_payment",
        "user"
    )

admin.site.register(CreditCardRecord, CreditCardRecordAdmin)