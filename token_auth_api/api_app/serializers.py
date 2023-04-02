from rest_framework import serializers 
from .models import Employee
from django.contrib.auth.models import User

# Employee serializer
class EmployeeSerializer(serializers.ModelSerializer):
    """Employee Serializer to serialize or de-serialize the fields of Emloyee models"""
    class Meta:
        model  = Employee
        fields = ('id', 'name', 'email', 'salary')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    