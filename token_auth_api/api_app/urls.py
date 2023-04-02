from django.urls import path
from . import views
# from rest_framework.authtoken.views import obtain_auth_token

from .auth_token import CustomAuthToken

urlpatterns = [
    path('employee-api/', views.EmployeeAPI.as_view(), name='employee_api'),
    path('employee-api/<int:id>/', views.EmployeeAPI.as_view(),),
    path('get-api-token/',CustomAuthToken.as_view()),
    
    # path('get-api-token/', views.GetAPIToken.as_view(),),
    # path('get-api-token/', obtain_auth_token),
    
    
    
    
    
    
    
]
