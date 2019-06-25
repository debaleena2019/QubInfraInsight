from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import const_spec

class const_spec_Serializer(serializers.ModelSerializer):
    class Meta:
        model=const_spec
        fields='__all__'
