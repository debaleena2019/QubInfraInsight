
from rest_framework import viewsets
from .serializers import po_customer_Serializer
from .models import po_customer

class po_customer_ViewSet(viewsets.ModelViewSet):
    queryset=po_customer.objects.all()
    serializer_class=po_customer_Serializer