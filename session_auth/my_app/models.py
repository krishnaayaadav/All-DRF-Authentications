
from django.db import models


STATUS = (
   ('publish', 'Publish'),
   ('pending', 'Pending'),

)
class Article(models.Model):
   title = models.CharField(max_length=250)
   author = models.CharField(max_length=100)
   description = models.TextField(max_length=250)

   created_at = models.DateTimeField(auto_now_add=True)
   status = models.CharField(max_length=50, default='pending')
   
   
   
   


