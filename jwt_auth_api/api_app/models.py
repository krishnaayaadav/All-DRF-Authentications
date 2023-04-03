from django.db import models

# Create your models here.


class Employee(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField(max_length=250, unique=True)
   salary = models.IntegerField()
