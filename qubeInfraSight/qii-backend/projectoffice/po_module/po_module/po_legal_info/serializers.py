from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import po_legal_info

class legal_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=po_legal_info
        fields='__all__'
