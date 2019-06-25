from django.db import models

class po_address(models.Model):
    add_id=models.CharField(max_length=32)
    com_id=models.CharField(max_length=32)
    add_type=models.CharField(max_length=32)
    add_address_line1=models.CharField(max_length=40)
    add_address_line2=models.CharField(max_length=40)
    add_city=models.CharField(max_length=20)
    add_country=models.CharField(max_length=20)
    add_pin=models.CharField(max_length=10)
    add_updated_on=models.DateTimeField(auto_now_add=True)
    add_updated_by=models.CharField(max_length=30)
   
    
