from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import po_project_att

class po_project_attSerializer(serializers.ModelSerializer):
    class Meta:
        model=po_project_att
        fields='__all__'
