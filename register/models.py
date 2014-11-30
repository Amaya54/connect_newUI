from django.db import models

# Create your models here.
class users(models.Model):
    userId = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    dob = models.CharField(max_length=10)
    location = models.CharField(max_length=500)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=200,primary_key=True)
    contactNo = models.CharField(max_length=200,unique=True)
    doj = models.DateTimeField(auto_now_add=True)
    flags = models.CharField(max_length=3)
    password = models.CharField(max_length=200)