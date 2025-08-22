from django.db import models

# Create your models here.
class enrollmentdetail(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=10)
    date=models.DateField()


  