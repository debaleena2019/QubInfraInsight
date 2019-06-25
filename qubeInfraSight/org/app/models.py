# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TblOrganization(models.Model):
    org_id = models.IntegerField(primary_key=True)
    org_name = models.CharField(max_length=50)
    org_level = models.CharField(max_length=20)
    org_country = models.CharField(max_length=20)
    org_code = models.CharField(max_length=20)
    org_currency = models.CharField(max_length=20)
    org_language = models.CharField(max_length=20)
    parent_org_id = models.CharField(max_length=20, blank=True, null=True)
    org_updated_on = models.DateTimeField(blank=True, null=True)
    org_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'tbl_organisation'


class TblAditionalAttribute(models.Model):
    addinfo_id = models.IntegerField(primary_key=True)
    org_id = models.ForeignKey(TblOrganization, related_name='additional_att',on_delete=models.CASCADE)
    addinfo_attr = models.CharField(max_length=20)
    addinfo_value = models.CharField(max_length=20)
    addinfo_updated_on = models.DateTimeField(blank=True, null=True)
    addinfo_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_additional_attribute'


class TblCommChannel(models.Model):
    com_id =  models.IntegerField(primary_key=True)
    org_id = models.ForeignKey(TblOrganization,related_name="comm_channel",on_delete=models.CASCADE)
    com_type = models.CharField(max_length=40)
    com_updated_on = models.DateTimeField(blank=True, null=True)
    com_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_comm_channel'


class TblAddress(models.Model):
    add_id =  models.IntegerField(primary_key=True)
    com_id = models.ForeignKey(TblCommChannel,related_name='comm_address',on_delete=models.CASCADE)
    add_type = models.CharField(max_length=20, blank=True, null=True)
    add_address_line1 = models.CharField(max_length=40, blank=True, null=True)
    add_addres_line2 = models.CharField(max_length=40, blank=True, null=True)
    add_city = models.CharField(max_length=20, blank=True, null=True)
    add_state = models.CharField(max_length=20, blank=True, null=True)
    add_country = models.CharField(max_length=20, blank=True, null=True)
    add_pin = models.CharField(max_length=10, blank=True, null=True)
    add_updated_on = models.DateTimeField(blank=True, null=True)
    add_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_address'



class TblEmail(models.Model):
    eml_id =  models.IntegerField(primary_key=True)
    com_id = models.ForeignKey(TblCommChannel,related_name='comm_email',on_delete=models.CASCADE)
    eml_address = models.CharField(max_length=40)
    eml_updated_on = models.DateTimeField(blank=True, null=True)
    eml_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_email'


class TblLegalInfo(models.Model):
    legalinfo_id =  models.IntegerField(primary_key=True,null=False)
    org_id = models.ForeignKey(TblOrganization,related_name='org_legal_info',on_delete=models.CASCADE)
    legalinfo_type = models.CharField(max_length=30)
    legalinfo_value = models.CharField(max_length=100, blank=True, null=True)
    legalinfo_updated_on = models.DateTimeField(blank=True, null=True)
    legalinfo_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_legal_info'




class TblPhone(models.Model):
    ph_id =  models.IntegerField(primary_key=True)
    com_id = models.ForeignKey(TblCommChannel,related_name='comm_phone',on_delete=models.CASCADE)
    ph_isd_code = models.CharField(max_length=10, blank=True, null=True)
    ph_std_code = models.CharField(max_length=10, blank=True, null=True)
    ph_no = models.CharField(max_length=15)
    ph_updated_on = models.DateTimeField(blank=True, null=True)
    ph_updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_phone'
