from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import po_emailSerializer
from .models import po_email

class po_emailViewSet(viewsets.ModelViewSet):
    queryset=po_email.objects.all()
    serializer_class=po_emailSerializer