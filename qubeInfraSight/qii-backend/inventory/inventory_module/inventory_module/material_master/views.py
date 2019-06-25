
from rest_framework import viewsets
from .serializers import mat_master_Serializer
from .models import mat_master

class mat_master_ViewSet(viewsets.ModelViewSet):
    queryset=mat_master.objects.all()
    serializer_class=mat_master_Serializer