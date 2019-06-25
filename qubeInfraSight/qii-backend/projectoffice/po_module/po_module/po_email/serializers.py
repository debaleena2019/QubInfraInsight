from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import po_email

class po_emailSerializer(serializers.ModelSerializer):
    class Meta:
        model=po_email
        fields='__all__'
