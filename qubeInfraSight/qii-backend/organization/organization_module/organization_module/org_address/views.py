
from rest_framework import viewsets
from .serializers import orgAddressSerializer
from .models import orgAddress

class orgaddressViewSet(viewsets.ModelViewSet):
    queryset=orgAddress.objects.all()
    serializer_class=orgAddressSerializer