
from rest_framework import serializers
from .models import additionaladdress

class additionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=additionaladdress
        fields='__all__'
