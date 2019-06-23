
from rest_framework import serializers
from .models import po_additional_att

class addtional_attributeSerializer(serializers.ModelSerializer):
    class Meta:
        model=po_additional_att
        fields='__all__'
