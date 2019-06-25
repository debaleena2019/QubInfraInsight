from django.db import models

class const_spec(models.Model):
    const_spec_id=models.CharField(max_length=32)
    const_spec_name=models.CharField(max_length=30)
    const_spec_unit_value=models.CharField(max_length=20)
    const_spec_unit=models.CharField(max_length=10)
    const_spec_updated_on=models.DateTimeField(auto_now_add=True)
    const_spec_updated_by=models.CharField(max_length=20)
   

    
