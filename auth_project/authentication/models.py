from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    username=models.CharField(max_length=10,unique=True)
    mobile_number=models.CharField(max_length=10,blank=True,null=True)
    email=models.EmailField(max_length=50)

class Store(models.Model):
    name=models.CharField(max_length=10)