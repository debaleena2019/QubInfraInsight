from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import mat_unit

class mat_unit_Serializer(serializers.ModelSerializer):
    class Meta:
        model=mat_unit
        fields='__all__'
