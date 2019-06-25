from django.db import models

class org(models.Model):
    org_id=models.CharField(max_length=32)
    org_name=models.CharField(max_length=50)
    org_level=models.CharField(max_length=20)
    org_country=models.CharField(max_length=20)
    org_code=models.CharField(max_length=20)
    org_currency=models.CharField(max_length=20)
    org_language=models.CharField(max_length=20)
    parent_org_id=models.CharField(max_length=20)
    org_updated_on=models.DateTimeField(auto_now_add=True)
    org_updated_by=models.CharField(max_length=20)
    