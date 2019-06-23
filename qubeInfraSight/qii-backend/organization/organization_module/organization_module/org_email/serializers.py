
from rest_framework import serializers
from .models import orgemail

class emailSerializer(serializers.ModelSerializer):
    class Meta:
        model=orgemail
        fields='__all__'
