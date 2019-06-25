from django.forms import forms
from rest_framework.views import APIView
from rest_framework import viewsets, request
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.utils import json
from django.db import transaction
from .models import TblAddress, TblAditionalAttribute, TblCommChannel, TblEmail, TblLegalInfo, TblOrganization, TblPhone
from .serializers import OrgSerializer,AdditionalAttributeSerializer,LegalInfoSerializer,CommChannnelSerializer,AddressSerializer,PhoneSerializer,EmailSerializer
# Create your views here.

class orgViewSet(viewsets.ModelViewSet):
    queryset=TblOrganization.objects.all()
    serializer_class = OrgSerializer

# class createOrg(APIView):
#     queryset=TblOrganization.objects.all()
#     @api_view(['GET','POST'])
#     def createorg(request):
#         if request.method=='POST':
#             return Response({"message": "Got some data!", "data": request.data})
        
class addressViewSet(viewsets.ModelViewSet):
    queryset=TblAddress.objects.all()
    serializer_class = AddressSerializer

class attributeViewSet(viewsets.ModelViewSet):
    queryset=TblAditionalAttribute.objects.all()
    serializer_class = AdditionalAttributeSerializer

class legalViewSet(viewsets.ModelViewSet):
    queryset=TblLegalInfo.objects.all()
    serializer_class = LegalInfoSerializer

class commViewSet(viewsets.ModelViewSet):
    queryset=TblCommChannel.objects.all()
    serializer_class = CommChannnelSerializer

class emailViewSet(viewsets.ModelViewSet):
    queryset=TblEmail.objects.all()
    serializer_class = EmailSerializer

class phoneViewSet(viewsets.ModelViewSet):
    queryset=TblPhone.objects.all()
    serializer_class = PhoneSerializer


@api_view(['GET','POST', 'PUT'])
def createorg(request):
    if request.method=="POST":
        serializer=OrgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        #print(request.data)
        return Response({"Organisation created, Data=": request.data.get('org_id')})
@transaction.atomic        
@api_view(['GET','POST'])
def updateorg(request):
    if request.method=="POST":
        additional_attr=request.data['additional_attributes'][0]
        serializer=AdditionalAttributeSerializer(data=additional_attr)
        print(additional_attr)
        #_, mesage = serializer.create()

        legal_info=request.data['org_legal_info'][0]
        legal_serializer=LegalInfoSerializer(data=legal_info)
        print(legal_info)
        #print(legal_serializer.data['legalinfo_type'])
        legal = legal_serializer.create()
       # print(legal)
        
        return Response({"Additional Attribute created, Data=":request.data['org_legal_info']})


