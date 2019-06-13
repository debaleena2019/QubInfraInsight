from rest_framework import serializers
from .models import Customer, CustomerCommChannel, Address, Project, CustomerAdditionalAttribute, Email, Phone, \
    ProjectAttributes, CustomerLegalInfo


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = '__all__'
        fields = ('name', 'code', 'type', 'updated_by')


class CustomerLegalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLegalInfo
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class CustomerCommChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCommChannel
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomerAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAdditionalAttribute
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAttributes
        fields = '__all__'
