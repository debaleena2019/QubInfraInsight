from django.db import models

class legaladdress(models.Model):
    legalinfo_id=models.CharField(max_length=32)
    org_id=models.CharField(max_length=32)
    legalinfo_type=models.CharField(max_length=30)
    legalinfo_value=models.CharField(max_length=100)
    legalinfo_updated_on=models.DateTimeField(auto_now_add=True)
    legalinfo_updated_by=models.CharField(max_length=20)
   
