from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import po_phone

class phoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=po_phone
        fields='__all__'
