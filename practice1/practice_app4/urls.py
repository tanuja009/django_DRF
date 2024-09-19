from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
   path('student_list/',views.LCUsersList.as_view(),name="student_list"), 
   path('userdata/<int:pk>/',views.RUDUsersListUser.as_view()),
   path('api-auth/', include('rest_framework.urls')), 
   
]