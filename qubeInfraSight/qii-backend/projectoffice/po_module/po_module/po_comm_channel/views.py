
from rest_framework import viewsets
from .serializers import po_comm_channelSerializer
from .models import po_comm_chanl

class po_comm_chanlViewSet(viewsets.ModelViewSet):
    queryset=po_comm_chanl.objects.all()
    serializer_class=po_comm_channelSerializer