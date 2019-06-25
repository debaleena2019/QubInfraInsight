from django.db import models

class po_project_att(models.Model):
    proj_att_id=models.CharField(max_length=32)
    project_id=models.CharField(max_length=32)
    proj_attribute=models.CharField(max_length=30)
    proj_value=models.CharField(max_length=30)
    proj_att_updated_on=models.DateTimeField(auto_now_add=True)
    proj_att_updated_by=models.CharField(max_length=30)
   
    
