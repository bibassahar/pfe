from django.db import models

# Create your models here.

class FilsManger(models.Model):
    file_number=models.IntegerField()
    uploded_by=models.IntegerField()
    uploded_at=models.DateTimeField()


