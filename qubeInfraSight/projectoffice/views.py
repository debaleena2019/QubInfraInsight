from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, CustomerCommChannel, Address, Project, CustomerAdditionalAttribute, Email, Phone, \
    ProjectAttributes
from .serializers import AddressSerializer, CustomerAdditionalInfoSerializer, EmailSerializer, PhoneSerializer, \
    ProjectAttributeSerializer, ProjectSerializer, CustomerSerializer, CustomerCommChannelSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class CustomerCommChannelViewSet(viewsets.ModelViewSet):
    queryset = CustomerCommChannel.objects.all()
    serializer_class = CustomerCommChannelSerializer


class CustomerAddInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomerAdditionalAttribute.objects.all()
    serializer_class = CustomerAdditionalInfoSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProjectAttributes.objects.all()
    serializer_class = ProjectAttributeSerializer
