from django.db import models
from register.models import * 
# Create your models here.
class login(models.Model):
	email = models.CharField(max_length=200,primary_key=True)
	contactNo = models.CharField(max_length=200,unique=True)
	password = models.CharField(max_length=200)
