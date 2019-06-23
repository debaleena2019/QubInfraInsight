from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import po_address

class po_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model=po_address
        fields='__all__'