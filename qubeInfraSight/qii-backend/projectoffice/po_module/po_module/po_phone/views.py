from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import phoneSerializer
from .models import po_phone

class po_phoneViewSet(viewsets.ModelViewSet):
    queryset=po_phone.objects.all()
    serializer_class=phoneSerializer