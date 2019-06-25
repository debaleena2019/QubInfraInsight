
from rest_framework import viewsets
from .serializers import legalSerializer
from .models import legaladdress

class legalViewSet(viewsets.ModelViewSet):
    queryset=legaladdress.objects.all()
    serializer_class=legalSerializer