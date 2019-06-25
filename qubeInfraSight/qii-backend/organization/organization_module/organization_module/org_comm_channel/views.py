
from rest_framework import viewsets
from .serializers import commchannelSerializer
from .models import orgcommchannel

class commchannelViewSet(viewsets.ModelViewSet):
    queryset=orgcommchannel.objects.all()
    serializer_class=commchannelSerializer