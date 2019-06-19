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
    # phone_set = PhoneSerializer(source='phone', many=True)
    # email_set = EmailSerializer(source='email', many=True)
    # address_set = AddressSerializer(source='address', many=True)
    phone_set = PhoneSerializer(many=True)
    email_set = EmailSerializer(many=True)
    address_set = AddressSerializer(many=True)

    class Meta:
        model = CustomerCommChannel
        fields = '__all__'

    def create(self, validated_data):
        phone_data = validated_data.pop('phone_set')
        email_data = validated_data.pop('email_set')
        address_data = validated_data.pop('address_set')
        comm_channel = CustomerCommChannel.objects.create(**validated_data)

        for phone_detail in phone_data:
            phone_detail, created = Phone.objects.get_or_create(name=phone_detail['phone'])
            comm_channel.phone_set.add(phone_detail)
        for email_detail in email_data:
            email_detail, created = Email.objects.get_or_create(name=email_detail['email'])
            comm_channel.email_set.add(email_detail)
        for address_detail in address_data:
            address_detail, created = Phone.objects.get_or_create(name=address_detail['line1'])
            comm_channel.address_set.add(address_detail)
        return comm_channel


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
