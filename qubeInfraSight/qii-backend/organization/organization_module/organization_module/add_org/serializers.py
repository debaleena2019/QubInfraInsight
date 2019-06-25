
from rest_framework import serializers
from .models import org

class orgSerializer(serializers.ModelSerializer):
    class Meta:
        model=org
        fields='__all__'
