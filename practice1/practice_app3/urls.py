from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
   path('',views.LCUsersList.as_view()), 
   path('userdata/<int:pk>/',views.RUDUsersListUser.as_view()),
   path('api-auth/', include('rest_framework.urls')), 
]