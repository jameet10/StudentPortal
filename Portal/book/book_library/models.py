from django.db import models

# Create your models here.
class enrollmentdetail(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=10)
    date=models.DateField()
    def __str__(self):
        return self.name



class PYQ(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.year})"
    


