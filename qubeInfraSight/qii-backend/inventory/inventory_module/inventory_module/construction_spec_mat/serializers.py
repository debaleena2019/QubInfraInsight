
from rest_framework import serializers
from .models import const_spec_mat

class const_spec_mat_Serializer(serializers.ModelSerializer):
    class Meta:
        model=const_spec_mat
        fields='__all__'
