from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
   path('student/', views.students_details.as_view(), name="student_details"),
   path('student/<int:id>/', views.students_details.as_view(), name="student_details"), 
   path('api-auth/', include('rest_framework.urls')), 
]