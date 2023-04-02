from django.contrib import admin
from .models import Employee



# Employee model registeration in admin panal
@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
   list_display = ('id', 'name', 'email', 'salary')