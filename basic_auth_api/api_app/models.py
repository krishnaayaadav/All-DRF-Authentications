from django.db import models
import time
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=77)
    email = models.EmailField(unique=True)
    salary = models.PositiveIntegerField()