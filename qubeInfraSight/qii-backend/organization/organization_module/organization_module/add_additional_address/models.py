from django.db import models

class additionaladdress(models.Model):
    addinfo_id=models.CharField(max_length=32)
    org_id=models.CharField(max_length=32)
    addinfo_attr=models.CharField(max_length=20)
    addinfo_value=models.CharField(max_length=20)
    addinfo_updated_on=models.DateTimeField(auto_now_add=True)
    addinfo_updated_by=models.CharField(max_length=20)
   
