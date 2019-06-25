from django.db import models

class po_project(models.Model):
    project_id=models.CharField(max_length=32)
    customer_id=models.CharField(max_length=32)
    project_name=models.CharField(max_length=30)
    project_code=models.CharField(max_length=30)
    project_type=models.CharField(max_length=30)
    project_updated_on=models.DateTimeField(auto_now_add=True)
    project_updated_by=models.CharField(max_length=30)
   
    
