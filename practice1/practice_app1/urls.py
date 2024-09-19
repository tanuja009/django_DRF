from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('student_info/', views.students_deatils.as_view(), name="task"),
    path('student_info/<int:id>/', views.students_deatils.as_view(), name="task"),
    path('api-auth/', include('rest_framework.urls')), 
    
]