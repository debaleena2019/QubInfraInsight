
from rest_framework import serializers
from .models import po_customer

class po_customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model=po_customer
        fields='__all__'