
from rest_framework import serializers
from .models import orgcommchannel

class commchannelSerializer(serializers.ModelSerializer):
    class Meta:
        model=orgcommchannel
        fields='__all__'
