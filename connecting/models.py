from django.db import models

# Create your models here.

class connectDetails(models.Model):
    connectId = models.CharField(max_length=200,primary_key=True)
    postId = models.CharField(max_length=200)
    userId = models.CharField(max_length=200)
    doc = models.DateTimeField(auto_now_add=True)
    exchangeFlag = models.CharField(max_length=6)

