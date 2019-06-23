from rest_framework import viewsets
from .serializers import orgSerializer
from .models import org

class organizationViewSet(viewsets.ModelViewSet):
    queryset=org.objects.all()
    serializer_class=orgSerializer