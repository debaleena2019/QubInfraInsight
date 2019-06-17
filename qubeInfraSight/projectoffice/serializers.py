from rest_framework import serializers

from .models import Customer, CustomerCommChannel, Address, Project, CustomerAdditionalAttribute, Email, Phone, \
    ProjectAttributes, CustomerLegalInfo


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        # fields = ('name', 'code', 'type', 'updated_by')


class CustomerLegalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLegalInfo
        depth = 1
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomerCommChannelSerializer(serializers.ModelSerializer):
    phone_set = PhoneSerializer(source='phone', many=True)
    email_set = EmailSerializer(source='email', many=True)
    address_set = AddressSerializer(source='address', many=True)

    class Meta:
        model = CustomerCommChannel
        fields = '__all__'


class CustomerAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAdditionalAttribute
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAttributes
        fields = '__all__'


class CustomerAggregatedSerializer(serializers.ModelSerializer):
    customerLegalInfo_set = CustomerLegalInfoSerializer(source='customer_legal_info', many=True)
    customerAdditionalAttribute_set = CustomerAdditionalInfoSerializer(source='customer_aditional_info', many=True)
    customerCommChannel_set = CustomerCommChannelSerializer(source='customer_comm_channel', many=True)

    class Meta:
        model = Customer
        fields = '__all__'
        # fields = ('name', 'code', 'type', 'updated_by')
