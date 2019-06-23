from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import po_comm_chanl

class po_comm_channelSerializer(serializers.ModelSerializer):
    class Meta:
        model=po_comm_chanl
        fields='__all__'
