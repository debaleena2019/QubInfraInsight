
from rest_framework import viewsets
from .serializers import const_spec_mat_Serializer
from .models import const_spec_mat

class const_spec_mat_ViewSet(viewsets.ModelViewSet):
    queryset=const_spec_mat.objects.all()
    serializer_class=const_spec_mat_Serializer