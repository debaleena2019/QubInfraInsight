from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import po_project


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model=po_project
        fields='__all__'
