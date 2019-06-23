from rest_framework import serializers
import sys, json

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

    customerLegalInfo_set = CustomerLegalInfoSerializer(source='customer_legal_info', many=True, read_only=True)
    customerAdditionalAttribute_set = CustomerAdditionalInfoSerializer(source='customer_additional_info', many=True, read_only=True)
    customerCommChannel_set = CustomerCommChannelSerializer(source='customer_comm_channel', many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        # fields = ('name', 'code', 'type', 'updated_by')

    def create(self, validated_data):
        print('INSIDE CREATE..........' + validated_data.get('name'))
        print('INSIDE CREATE..........' + validated_data.get('customer_additional_info'))
        #additional_attributes_data = validated_data.pop('customer_additional_info')
        #customer_legal_data = validated_data.pop('customer_legal_info')
        #customer_commChannel_data = validated_data.pop('customer_comm_channel')

        try:
            Customer.objects.create(**validated_data)
            # for add_attribute in additional_attributes_data:
            #     CustomerAdditionalAttribute.objects.create(**add_attribute)
        except:
            # Prints the error and the line that causes the error
            print("%s - %s at line: %s" % (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))

