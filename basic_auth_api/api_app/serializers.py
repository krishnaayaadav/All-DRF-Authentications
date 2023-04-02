from rest_framework import serializers 
from .models import Employee

# Employee serializer
class EmployeeSerializer(serializers.ModelSerializer):
    """Employee Serializer to serialize or de-serialize the fields of Emloyee models"""
    class Meta:
        model  = Employee
        fields = ('id', 'name', 'email', 'salary')