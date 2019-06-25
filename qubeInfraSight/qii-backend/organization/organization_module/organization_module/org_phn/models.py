from django.db import models

class orgphone(models.Model):
    ph_id=models.CharField(max_length=32)
    com_id=models.CharField(max_length=32)
    ph_isd_code=models.CharField(max_length=10)
    ph_std_code=models.CharField(max_length=10)
    ph_no=models.CharField(max_length=15)
    ph_updated_on=models.DateTimeField(auto_now_add=True)
    ph_updated_by=models.CharField(max_length=20)
   

    
