from rest_framework import serializers
from .models import Debtors

class DebtorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debtors
        fields = '__all__'