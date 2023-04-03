from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
   list_display = ('id', 'name', 'salary', 'email')
