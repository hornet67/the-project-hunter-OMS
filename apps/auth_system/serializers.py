from rest_framework import serializers
from .models import PendingCompany


class PendingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingCompany
        fields = ['company_name','email','phone_number','website','domain']
        