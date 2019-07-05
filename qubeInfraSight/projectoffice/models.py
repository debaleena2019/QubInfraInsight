from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_code = models.CharField(max_length=100)
    customer_type = models.CharField(max_length=100)
    customer_tag = models.CharField(max_length=100)
    customer_updated_on = models.DateTimeField(blank=True, null=True)
    customer_updated_by = models.CharField(max_length=100)
    status = models.CharField(max_length=20, null=False)

    class Meta:
        managed = False
        db_table = 'tbl_customer'

    def __str__(self):

        return str(self.customer_id)


class CustomerLegalInfo(models.Model):
    legalinfo_id = models.AutoField(max_length=100, primary_key=True)
    customer = models.ForeignKey(Customer, related_name='legal_info', on_delete=models.CASCADE)
    legalinfo_type = models.CharField(max_length=100)
    legalinfo_value = models.CharField(max_length=100)
    legalinfo_updated_on = models.DateTimeField(auto_now=True)
    legalinfo_updated_by = models.CharField(max_length=100)
    status = models.CharField(max_length=20,null=False)

    class Meta:
        unique_together = ('customer', 'legalinfo_id')
        managed = False
        db_table = 'tbl_legal_info'

class Project(models.Model):
    project_id = models.CharField(max_length=100, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=32)
    project_code = models.CharField(max_length=32)
    project_type = models.CharField(max_length=32)
    project_updated_on = models.DateTimeField(auto_now=True)
    project_updated_by = models.CharField(max_length=32)
    status = models.CharField(max_length=20, null=False)

    class Meta:
        unique_together = ('customer', 'project_id')
        managed = False
        db_table = 'tbl_project'
#
#
class ProjectAttributes(models.Model):
    proj_att_id = models.AutoField(max_length=100, primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    proj_attribute = models.CharField(max_length=32)
    proj_value = models.CharField(max_length=32)
    proj_att_updated_on = models.DateTimeField(auto_now=True)
    proj_att_updated_by = models.CharField(max_length=32)
    status = models.CharField(max_length=20, null=False)

    class Meta:
        unique_together = ('project', 'proj_att_id')
        managed = False
        db_table = 'tbl_project_attributes'
#
#
class CustomerAdditionalAttribute(models.Model):
    addinfo_id = models.AutoField(max_length=20, primary_key=True)
    customer = models.ForeignKey(Customer, related_name='additional_attributes', on_delete=models.CASCADE)
    addinfo_attr = models.CharField(max_length=20)
    addinfo_value = models.CharField(max_length=20)
    addinfo_updated_on = models.DateTimeField(auto_now=True)
    addinfo_updated_by = models.CharField(max_length=20)
    status = models.CharField(max_length=20, null=False)

    class Meta:
        managed = False
        unique_together = ('customer', 'addinfo_id')
        db_table = 'tbl_customer_aditional_attribute'


# class CustomerCommChannel(models.Model):
#     id = models.CharField(max_length=32, primary_key=True)
#     customer_id = models.ForeignKey(Customer, related_name='customer_comm_channel', on_delete=models.CASCADE)
#     comm_type = models.CharField(max_length=32)
#     updated_on = models.DateTimeField(auto_now=True)
#     updated_by = models.CharField(max_length=20)
#
#
class Phone(models.Model):
    ph_id = models.AutoField(max_length=32, primary_key=True)
    customer = models.ForeignKey(Customer, related_name='phone', on_delete=models.CASCADE)
    ph_isd_code = models.CharField(max_length=32)
    ph_std_code = models.CharField(max_length=32)
    ph_no = models.CharField(max_length=32)
    ph_updated_on = models.DateTimeField(auto_now=True)
    ph_updated_by = models.CharField(max_length=20)
    status = models.CharField(max_length=20, null=False)

    class Meta:
        managed = False
        unique_together = ('customer', 'ph_id')
        db_table = 'tbl_phone'
#
#
class Email(models.Model):
    eml_id = models.CharField(max_length=32, primary_key=True)
    customer = models.ForeignKey(Customer, related_name='email', on_delete=models.CASCADE)
    eml_address = models.CharField(max_length=32)
    eml_updated_on = models.DateTimeField(auto_now=True)
    eml_updated_by = models.CharField(max_length=20)
    status = models.CharField(max_length=20, null=False)

    class Meta:
        managed = False
        unique_together = ('customer', 'eml_id')
        db_table = 'tbl_email'


class Address(models.Model):
    add_id = models.AutoField(max_length=32, primary_key=True)
    customer = models.ForeignKey(Customer, related_name='address', on_delete=models.CASCADE)
    add_type = models.CharField(max_length=32)
    add_address_line1 = models.CharField(max_length=32)
    add_addres_line2 = models.CharField(max_length=32)
    add_city = models.CharField(max_length=32)
    add_state = models.CharField(max_length=32)
    add_country = models.CharField(max_length=32)
    add_pin = models.CharField(max_length=32)
    add_updated_on = models.DateTimeField(auto_now=True)
    add_updated_by = models.CharField(max_length=20)
    status = models.CharField(max_length=20, null=False)

    class Meta:
        managed = False
        unique_together = ('customer', 'add_id')
        db_table = 'tbl_address'
