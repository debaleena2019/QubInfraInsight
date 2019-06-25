from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import legal_infoSerializer
from .models import po_legal_info

class po_legal_infoViewSet(viewsets.ModelViewSet):
    queryset=po_legal_info.objects.all()
    serializer_class=legal_infoSerializer