from django.forms import forms
from rest_framework.views import APIView
from rest_framework import viewsets, request
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.utils import json
from django.db import transaction

#from .models import Customer, CustomerCommChannel, Address, Project, CustomerAdditionalAttribute, Email,Phone,ProjectAttributes, CustomerLegalInfo
from .models import Customer,CustomerAdditionalAttribute,CustomerLegalInfo
from .serializers import CustomerAdditionalInfoSerializer,CustomerSerializer,CustomerLegalInfoSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# class AddressViewSet(viewsets.ModelViewSet):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#
#
# class EmailViewSet(viewsets.ModelViewSet):
#     queryset = Email.objects.all()
#     serializer_class = EmailSerializer
#

class LegalInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomerLegalInfo.objects.all()
    serializer_class = CustomerLegalInfoSerializer


# class CustomerCommChannelViewSet(viewsets.ModelViewSet):
#     queryset = CustomerCommChannel.objects.all()
#     serializer_class = CustomerCommChannelSerializer
#

class CustomerAddInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomerAdditionalAttribute.objects.all()
    serializer_class = CustomerAdditionalInfoSerializer


# class PhoneViewSet(viewsets.ModelViewSet):
#     queryset = Phone.objects.all()
#     serializer_class = PhoneSerializer


# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class ProjectAttributeViewSet(viewsets.ModelViewSet):
#     queryset = ProjectAttributes.objects.all()
#     serializer_class = ProjectAttributeSerializer
#
#
# class CustomerAggregateViewSet(viewsets.ModelViewSet):
#     # queryset = Customer.objects.all().select_related()
#     queryset = Customer.objects.all()
#     serializer_class = CustomerAggregatedSerializer


#@api_view(['GET', 'POST'])
#def customer_list(request, format=None):
#    """
#     List all customer, or search a specific customer.
#     """
#     if request.method == 'GET':
#         print('inside GET................')
#         # snippets = Snippet.objects.all()
#         # serializer = SnippetSerializer(snippets, many=True)
#         return Response('')
#
#     elif request.method == 'POST':
#         print('inside POST................')
#         # serializer = SnippetSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response('')
# @api_view(['GET', 'POST', 'PUT'])
@api_view(['POST'])
def createcust(request):
    if request.method == "POST":
        # serializer = CustomerSerializer(data=request.data)
        serializer = CustomerSerializer()
        print(serializer)
        print(serializer.initial_data)
        serializer.create(request.data)
        return Response({"customer created, Data="})

        # if serializer.is_valid():
        #     serializer.save()
        # # print(request.data)
        # return Response({"customer created, Data=": request.data.get('org_id')})


# @transaction.atomic
# @api_view(['GET', 'POST'])
# def updatecust(request):
#     if request.method == "POST":
#         additional_attr = request.data['additional_attributes'][0]
#         serializer = CustomerAdditionalInfoSerializer(data=additional_attr)
#         print(additional_attr)
#         # _, mesage = serializer.create()
#
#         legal_info = request.data['cust_legal_info'][0]
#         legal_serializer = CustomerLegalInfoSerializer(data=legal_info)
#         print(legal_info)
#         # print(legal_serializer.data['legalinfo_type'])
#         legal = legal_serializer.create()
#         # print(legal)
#
#         return Response({"Additional Attribute created, Data=": request.data['cust_legal_info']})
#
#
