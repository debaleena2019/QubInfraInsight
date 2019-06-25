
from rest_framework import viewsets
from .serializers import additionalSerializer
from .models import additionaladdress

class additionalViewSet(viewsets.ModelViewSet):
    queryset=additionaladdress.objects.all()
    serializer_class=additionalSerializer