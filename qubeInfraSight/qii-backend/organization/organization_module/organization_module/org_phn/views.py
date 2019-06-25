
from rest_framework import viewsets
from .serializers import phoneSerializer
from .models import orgphone

class phoneViewSet(viewsets.ModelViewSet):
    queryset=orgphone.objects.all()
    serializer_class=phoneSerializer