from django.db import models

class po_legal_info(models.Model):
    legalinfo_id=models.CharField(max_length=32)
    customer_id=models.CharField(max_length=32)
    legalinfo_type=models.CharField(max_length=30)
    legalinfo_value=models.CharField(max_length=100)
    legalinfo_updated_on=models.DateTimeField(auto_now_add=True)
    legal_info_updated_by=models.CharField(max_length=30)
   
    
