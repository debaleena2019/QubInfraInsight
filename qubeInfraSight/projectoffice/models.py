from django.db import models


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tao = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)

    # class Meta:
    #     managed = False
    #     db_table = 'XXXXXXX'


class CustomerLegalInfo(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    customer_id = models.ForeignKey(Customer, related_name='customer_legal_info', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)


class Project(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=32)
    project_code = models.CharField(max_length=32)
    project_type = models.CharField(max_length=32)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=32)


class ProjectAttributes(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_attribute = models.CharField(max_length=32)
    project_value = models.CharField(max_length=32)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=32)


class CustomerAdditionalAttribute(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    customer_id = models.ForeignKey(Customer, related_name='customer_aditional_info', on_delete=models.CASCADE)
    add_attribute = models.CharField(max_length=20)
    add_value = models.CharField(max_length=20)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=20)


class CustomerCommChannel(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    customer_id = models.ForeignKey(Customer, related_name='customer_comm_channel', on_delete=models.CASCADE)
    comm_type = models.CharField(max_length=32)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=20)


class Phone(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    comm_id = models.ForeignKey(CustomerCommChannel, related_name='phone', on_delete=models.CASCADE)
    isd_code = models.CharField(max_length=32)
    std_code = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=20)


class Email(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    comm_id = models.ForeignKey(CustomerCommChannel, related_name='email', on_delete=models.CASCADE)
    email = models.CharField(max_length=32)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=20)


class Address(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    comm_id = models.ForeignKey(CustomerCommChannel, related_name='address', on_delete=models.CASCADE)
    add_type = models.CharField(max_length=32)
    line1 = models.CharField(max_length=32)
    line2 = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    pin = models.CharField(max_length=32)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=20)
