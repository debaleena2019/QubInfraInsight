from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, CustomerAdditionalAttribute, CustomerLegalInfo
from .serializers import CustomerAdditionalInfoSerializer, CustomerSerializer, \
    CustomerLegalInfoSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


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


@api_view(['POST', 'PUT', 'GET','DELETE'])
def createcust(request):
    if request.method == "POST":
        serializer = CustomerSerializer()
        serializer.create(request.data)
        return Response({"customer created, Data="})
    if request.method == "PUT":
        print("inside update")
        customer_id = request.data['customer_id']
        customer = Customer.objects.get(pk=customer_id)
        print(customer)
        print(customer_id)
        serializer = CustomerSerializer()
        serializer.update(customer, request.data) # instance is customer and data input is validated data
        print("inside update")
        return Response({"update cust, Data="})
    if request.method == 'GET':
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response({"customer": serializer.data})
# @api_view(['DELETE'])
def deleteData(request):
    if request.method=='DELETE':
        cust = Customer.objects.filter(pk=request.data['customer_id'])
        cust.delete()
        return Response({"deleted ( for id ) :":cust})
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
# class PhoneViewSet(viewsets.ModelViewSet):
#     queryset = Phone.objects.all()
#     serializer_class = PhoneSerializer


# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
# class AddressViewSet(viewsets.ModelViewSet):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#
#
# class EmailViewSet(viewsets.ModelViewSet):
#     queryset = Email.objects.all()
#     serializer_class = EmailSerializer
#
