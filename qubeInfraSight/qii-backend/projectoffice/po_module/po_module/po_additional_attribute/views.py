
from rest_framework import viewsets
from .serializers import addtional_attributeSerializer
from .models import po_additional_att

class po_additionalViewSet(viewsets.ModelViewSet):
    queryset=po_additional_att.objects.all()
    serializer_class=addtional_attributeSerializer