from django.db import models

class mat_master(models.Model):
    mate_id=models.CharField(max_length=32)
    mate_name=models.CharField(max_length=40)
    mate_code=models.CharField(max_length=20)
    mate_type=models.CharField(max_length=30)
    mate_desc=models.CharField(max_length=30)
    mate_updated_on=models.DateTimeField(auto_now_add=True)
    mate_updated_by=models.CharField(max_length=20)
   

    
