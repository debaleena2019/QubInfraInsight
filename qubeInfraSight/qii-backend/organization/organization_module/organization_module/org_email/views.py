

from rest_framework import viewsets
from .serializers import emailSerializer
from .models import orgemail

class emailViewSet(viewsets.ModelViewSet):
    queryset=orgemail.objects.all()
    serializer_class=emailSerializer