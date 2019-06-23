
from rest_framework import serializers
from .models import mat_master

class mat_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=mat_master
        fields='__all__'
