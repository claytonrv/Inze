from rest_framework import serializers

from django.contrib.auth.models import User

from credit_card.models import CreditCardRecord, CreditCardBillFile

class CreditCardRecordListSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.CharField(allow_blank=True)
    store = serializers.CharField(allow_blank=True)
    installment_total = serializers.IntegerField()
    installment_payment = serializers.IntegerField()
    user = serializers.CharField(source="user.username", read_only=True)
    file = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = CreditCardRecord
        fields = ("id", "day", "month", "year", "amount", "category", "store", "installment_total", "installment_payment", "user", "file")

    def get_day(self, record):
        return record.date.day

    def get_month(self, record):
        return record.date.month

    def get_year(self, record):
        return record.date.year


class CreditCardRecordSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d", input_formats=['%d-%m-%Y', 'iso-8601'])
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.CharField(allow_blank=True)
    store = serializers.CharField(allow_blank=True)
    installment_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    installment_payment = serializers.IntegerField()
    user = serializers.PrimaryKeyRelatedField(
        allow_null=False, required=True, queryset=User.objects.all()
    )
    file = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = CreditCardRecord
        fields = ("date", "amount", "category", "store", "installment_total", "installment_payment", "user", "file")
    
    def create(self, validated_data):
        return CreditCardRecord.objects.create(**validated_data)
