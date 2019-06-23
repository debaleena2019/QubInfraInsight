from rest_framework import serializers
from .models import TblAddress, TblAditionalAttribute, TblCommChannel, TblEmail, TblLegalInfo, TblOrganization, TblPhone

class AdditionalAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblAditionalAttribute
        fields='__all__'
    def create(self):
        add_attr_table=TblAditionalAttribute.objects.create()
        return add_attr_table, "additional serializer"

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblPhone
        fields='__all__'
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblAddress
        fields='__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblEmail
        fields='__all__'

class CommChannnelSerializer(serializers.ModelSerializer):
    comm_channel_phone=PhoneSerializer(source='comm_phone',many=True)
    comm_channel_email=EmailSerializer(source='comm_email',many=True)
    comm_channel_address=AddressSerializer(source='comm_address',many=True)
    class Meta:
        model=TblCommChannel
        fields='__all__'


class LegalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblLegalInfo
        fields='__all__'
    def create(self):
        legal_info=TblLegalInfo.objects.create()
        return legal_info

# serializer for create Organization & Search Organization
class OrgSerializer(serializers.ModelSerializer):
    additional_attributes=AdditionalAttributeSerializer(source='additional_att',many=True,read_only=True)
    comm_channel=CommChannnelSerializer(many=True,read_only=True)
    org_legal_info=LegalInfoSerializer(many=True,read_only=True)
    class Meta:
        model=TblOrganization
        fields='__all__'
    def save(self, validate_data):
        orgtable=TblOrganization.objects.update_or_create(**validate_data)
        return orgtable
    
class UpdateOrgSerializer(serializers.ModelSerializer):
    additional_attributes=AdditionalAttributeSerializer(source='additional_att',many=True)
    comm_channel=CommChannnelSerializer(many=True,read_only=True)
    org_legal_info=LegalInfoSerializer(many=True,read_only=True)
    class Meta:
        model=TblOrganization
        fields='__all__'
    def create(self, validate_data):
        additional_attrs=validate_data.pop('additional_attributes')
            # legal_infos=validate_data.pop('org_legal_info')
            # comm_channels=validate_data.pop('comm_channel')
        orgtable=TblOrganization.objects.create(**validate_data)
        for addattrs in additional_attrs:
            TblAditionalAttribute.objects.create(orgtable=orgtable,**addattrs)
            # for legals in legal_infos:
            #     TblLegalInfo.objects.create(legals)
        return orgtable
        
    def update(self, instance, validate_data):
        orgtable=TblOrganization.objects.update(**validate_data)
        orgtable.save()
        return orgtable

