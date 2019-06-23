from django.db import models

class po_additional_att(models.Model):
    addinfo_id=models.CharField(max_length=32)
    customer_id=models.CharField(max_length=32)
    addinfo_attr=models.CharField(max_length=30)
    addinfo_value=models.CharField(max_length=30)
    addinfo_updated_on=models.DateTimeField(auto_now_add=True)
    addinfo_updated_by=models.CharField(max_length=30)
   
    
