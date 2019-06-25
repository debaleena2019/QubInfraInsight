
from rest_framework import serializers
from .models import legaladdress

class legalSerializer(serializers.ModelSerializer):
    class Meta:
        model=legaladdress
        fields='__all__'
