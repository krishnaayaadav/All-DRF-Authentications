
from rest_framework import viewsets

from .models import Employee
from .serializers import EmployeeSerializer

# JWT imports 
from rest_framework_simplejwt.authentication import JWTAuthentication

# permission imports
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions

class EmployeeAPI(viewsets.ModelViewSet):
   
   authentication_classes = [JWTAuthentication]
   permission_classes     = [DjangoModelPermissions]
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer
   
   
