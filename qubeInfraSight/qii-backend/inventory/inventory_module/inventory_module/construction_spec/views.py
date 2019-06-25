
from rest_framework import viewsets
from .serializers import const_spec_Serializer
from .models import const_spec

class const_spec_ViewSet(viewsets.ModelViewSet):
    queryset=const_spec.objects.all()
    serializer_class=const_spec_Serializer