from django.db import models

# Create your models here.
class Attendence(models.Model):
    usn=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
