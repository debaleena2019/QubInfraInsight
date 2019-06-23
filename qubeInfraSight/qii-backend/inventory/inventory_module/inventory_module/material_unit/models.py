from django.db import models

class mat_unit(models.Model):
    mat_unit_id=models.CharField(max_length=32)
    mate_id=models.CharField(max_length=32)
    mat_unit_type=models.CharField(max_length=20)
    mat_unit_updated_on=models.DateTimeField(auto_now_add=True)
    mat_unit_updated_by=models.CharField(max_length=20)
   

    
