from django.db import models

# Create your models here.

class Info(models.Model):
    Name=models.CharField(max_length=20, default="")
    Age=models.IntegerField(default="")
    Qualification=models.CharField(max_length=50, default="")
    Address=models.CharField(max_length=100, default="")
    PhoneNo=models.IntegerField(default="")
    Email=models.CharField(max_length=30, default="")
