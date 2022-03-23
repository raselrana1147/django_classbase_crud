from distutils.command.upload import upload
from email.mime import image
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models

# Create your models here.

class Adminssion(models.Model):
    name=models.CharField(max_length=191,blank=True)
    email=models.EmailField(max_length=191,blank=True)
    phone=models.CharField(max_length=191,blank=True)
    father_name=models.CharField(max_length=191,blank=True)
    mother_name=models.CharField(max_length=191,blank=True)
    image=models.ImageField(upload_to='profile/',max_length=1000)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
