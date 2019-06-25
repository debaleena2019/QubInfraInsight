from django.db import models

class po_customer(models.Model):
    customer_id=models.CharField(max_length=32)
    customer_name=models.CharField(max_length=30)
    customer_code=models.CharField(max_length=30)
    customer_type=models.CharField(max_length=30)
    customer_tag=models.CharField(max_length=30)
    customer_updated_on=models.DateTimeField(auto_now_add=True)
    customer_updated_by=models.CharField(max_length=30)
   
