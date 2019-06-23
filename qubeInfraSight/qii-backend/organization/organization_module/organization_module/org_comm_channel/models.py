from django.db import models

class orgcommchannel(models.Model):
    com_id=models.CharField(max_length=32)
    org_id=models.CharField(max_length=32)
    com_type=models.CharField(max_length=40)
    com_updated_on=models.DateTimeField(auto_now_add=True)
    com_updated_by=models.CharField(max_length=20)
   
