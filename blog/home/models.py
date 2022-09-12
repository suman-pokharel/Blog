from email import message
import email
from msilib.schema import Class
from time import time
from unicodedata import name
from django.db import models
from matplotlib import image


# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=700)
    message=models.TextField()



    def __str__(self):
      return self.name


class Feedback(models.Model):
    name=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    comment=models.TextField()
    image=models.TextField()
    def __str__(self):
      return self.name

class Informations(models.Model):
  address1=models.CharField(max_length=100)
  address2=models.CharField(max_length=100)
  phone=models.CharField(max_length=100)
  time=models.CharField(max_length=100)
  email=models.EmailField(max_length=100)

  def __str__(self):
      return f"{self.address1} {self.address2}"


# class Service(models.Model):
  