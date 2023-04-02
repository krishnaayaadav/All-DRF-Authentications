from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# custom token
class CustomAuthToken(ObtainAuthToken):
   
   """to get custom authentication token"""
   
   def post(self, request, *args, **kwargs):
      """handling post request only"""
      
      # here I am serializing the request data
      serializer = self.serializer_class(data=request.data, context = {'request': request})
      
      if serializer.is_valid():
         
         # than we getting here user from validated_data
         user       = serializer.validated_data['user']
         
         # getting or creating that user token
         user_token, created = Token.objects.get_or_create(user=user)
         
         response   = { # making just dict here
            'username': user.username,      # user ka username
            'token': user_token.key,  # user token key
            'email': user.email       # user ka email hai
            
         }
         
         return Response(response, status=status.HTTP_200_OK)
      
      else:
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)