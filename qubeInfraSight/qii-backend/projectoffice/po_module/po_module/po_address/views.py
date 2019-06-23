
from rest_framework import viewsets
from .serializers import po_addressSerializer
from .models import po_address

class po_addressieViewSet(viewsets.ModelViewSet):
    queryset=po_address.objects.all()
    serializer_class=po_addressSerializer