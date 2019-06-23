
from rest_framework import serializers
from .models import orgAddress

class orgAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=orgAddress
        fields='__all__'
