from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_user_api_auth_token(sender=None, instance=None, created=False, *args, **kwargs):
   """to automatically create api token for new reigstered users """
   
   if created: # if user instance is create than create user api token
      
      print('\n \n \n New User is created ')
      Token.objects.create(user=instance)
      