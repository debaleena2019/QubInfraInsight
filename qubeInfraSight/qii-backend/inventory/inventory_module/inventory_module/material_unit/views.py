from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import mat_unit_Serializer
from .models import mat_unit

class mat_unit_ViewSet(viewsets.ModelViewSet):
    queryset=mat_unit.objects.all()
    serializer_class=mat_unit_Serializer