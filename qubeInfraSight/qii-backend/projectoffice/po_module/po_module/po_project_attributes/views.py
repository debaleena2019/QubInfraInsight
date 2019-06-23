from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import po_project_attSerializer
from .models import po_project_att

class po_projectAttViewSet(viewsets.ModelViewSet):
    queryset=po_project_att.objects.all()
    serializer_class=po_project_attSerializer