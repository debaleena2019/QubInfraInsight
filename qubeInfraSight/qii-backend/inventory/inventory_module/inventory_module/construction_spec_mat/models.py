from django.db import models

class const_spec_mat(models.Model):
    const_spec_mat_id=models.CharField(max_length=32)
    const_spec_id=models.CharField(max_length=32)
    mate_id=models.CharField(max_length=30)
    const_spec_mat_quantity=models.CharField(max_length=100)
    const_spec_mat_unit=models.CharField(max_length=100)
    const_spect_mat_updated_on=models.DateTimeField(auto_now_add=True)
    const_spect_mat_by=models.CharField(max_length=20)
   

    
