from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import projectSerializer
from .models import po_project

class po_projectViewSet(viewsets.ModelViewSet):
    queryset=po_project.objects.all()
    serializer_class=projectSerializer