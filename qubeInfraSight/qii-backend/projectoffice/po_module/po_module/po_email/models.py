from django.db import models

class po_email(models.Model):
    eml_id=models.CharField(max_length=32)
    com_id=models.CharField(max_length=32)
    eml_address=models.CharField(max_length=40)
    eml_updated_on=models.DateTimeField(auto_now_add=True)
    eml_updated_by=models.CharField(max_length=30)
   
    
