
from rest_framework import serializers
from .models import orgphone

class phoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=orgphone
        fields='__all__'
