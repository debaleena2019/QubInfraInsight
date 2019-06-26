from rest_framework import serializers

# from .models import Customer, CustomerCommChannel, Address, Project, CustomerAdditionalAttribute, Email, Phone, \
#     ProjectAttributes, CustomerLegalInfo
from .models import Customer, CustomerAdditionalAttribute, CustomerLegalInfo
from rest_framework.decorators import api_view

class CustomerAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAdditionalAttribute
        fields = '__all__'


class CustomerLegalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLegalInfo
        #    depth = 1
        fields = '__all__'

    # def create(self):
    #     legal_info = CustomerLegalInfo.objects.create()
    #     return legal_info


class CustomerSerializer(serializers.ModelSerializer):
    additional_attributes = CustomerAdditionalInfoSerializer(source='customer_additional_info', many=True)

    legal_info = CustomerLegalInfoSerializer(source='customer_legal_info', many=True)

    class Meta:
        model = Customer
        fields = '__all__'
        # fields = ('name', 'code', 'type', 'updated_by')

    def create(self, validate_data):
        additional_attrs = validate_data.pop('customer_additional_info')
        # print(additional_attrs)
        legal_infos = validate_data.pop('customer_legal_info')
        # print(legal_infos)
        # comm_channels=validate_data.pop('comm_channel')
        custable = Customer.objects.create(**validate_data)
        for addattrs in additional_attrs:
            CustomerAdditionalAttribute.objects.create(customer_id=custable, **addattrs)
        #CustomerAdditionalAttribute.objects.create(customer_id=custable, **additional_attrs)
        for legals in legal_infos:
            CustomerLegalInfo.objects.create(customer_id=custable, **legals)
        return custable

# class PhoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Phone
#         fields = '__all__'
#
#
# class EmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Email
#         fields = '__all__'
#
#
# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = '__all__'
#
#
# class CustomerCommChannelSerializer(serializers.ModelSerializer):
#     # phone_set = PhoneSerializer(source='phone', many=True)
#     # email_set = EmailSerializer(source='email', many=True)
#     # address_set = AddressSerializer(source='address', many=True)
#     phone_set = PhoneSerializer(source='comm_phone',many=True)
#     email_set = EmailSerializer(source='comm_email',many=True)
#     address_set = AddressSerializer(source='comm_address',many=True)
#
#
#     class Meta:
#         model = CustomerCommChannel
#         fields = '__all__'
#
# def create(self, validated_data):
#     phone_data = validated_data.pop('phone_set')
#     email_data = validated_data.pop('email_set')
#     address_data = validated_data.pop('address_set')
#     comm_channel = CustomerCommChannel.objects.create(**validated_data)
#
#     for phone_detail in phone_data:
#         phone_detail, created = Phone.objects.get_or_create(name=phone_detail['phone'])
#         comm_channel.phone_set.add(phone_detail)
#     for email_detail in email_data:
#         email_detail, created = Email.objects.get_or_create(name=email_detail['email'])
#         comm_channel.email_set.add(email_detail)
#     for address_detail in address_data:
#         address_detail, created = Phone.objects.get_or_create(name=address_detail['line1'])
#         comm_channel.address_set.add(address_detail)
#     return comm_channel


# class CustomerAdditionalInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerAdditionalAttribute
#         fields = '__all__'
# def create(self):
#     add_attr_table=CustomerAdditionalAttribute.objects.create()
#     return add_attr_table, "additional serializer"


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class ProjectAttributeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectAttributes
#         fields = '__all__'


# class CustomerAggregatedSerializer(serializers.ModelSerializer):
#     customerLegalInfo_set = CustomerLegalInfoSerializer(source='customer_legal_info', many=True)
#     customerAdditionalAttribute_set = CustomerAdditionalInfoSerializer(source='customer_aditional_info', many=True)
#     customerCommChannel_set = CustomerCommChannelSerializer(source='customer_comm_channel', many=True)
#
#     class Meta:
#         model = Customer
#         fields = '__all__'
#         # fields = ('name', 'code', 'type', 'updated_by')


# serializer for create customer & Search customer
# class CustomerAggregatedSerializer(serializers.ModelSerializer):
#     additional_attributes = CustomerAdditionalInfoSerializer(source='customer_additional_info', many=True, read_only=True)
#     customer_comm_channel = CustomerCommChannelSerializer(many=True, read_only=True)
#     customer_legal_info = CustomerLegalInfoSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Customer
#         fields = '__all__'
#
#     def save(self, validate_data):
#         custtable = Customer.objects.update_or_create(**validate_data)
#         return custtable


# class UpdateCustSerializer(serializers.ModelSerializer):
#     additional_attributes = CustomerAdditionalInfoSerializer(source='customer_additional_info', many=True)
#     customer_comm_channel = CustomerCommChannelSerializer(many=True, read_only=True)
#     customer_legal_info = CustomerLegalInfoSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Customer
#         fields = '__all__'
#
#     def create(self, validate_data):
#         additional_attrs = validate_data.pop('additional_attributes')
#         # legal_infos=validate_data.pop('org_legal_info')
#         # comm_channels=validate_data.pop('comm_channel')
#         custable = Customer.objects.create(**validate_data)
#         for addattrs in additional_attrs:
#             CustomerAdditionalAttribute.objects.create(custable=custable, **addattrs)
#             # for legals in legal_infos:
#             #     TblLegalInfo.objects.create(legals)
#         return custable
#
#     def update(self, instance, validate_data):
#         custable = Customer.objects.update(**validate_data)
#         custable.save()
#         return custable
