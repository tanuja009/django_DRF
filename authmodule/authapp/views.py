from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .models import *
# # Create your views here.
# #there is use authentication in local mode but you need to apply authentication globaly so code add in setting.py file 
# class RouteSerializer(viewsets.ModelViewSet):
#   queryset=student.objects.all()
#   serializer_class=RouteSerializer
#   # authentication_classes=[BasicAuthentication]
#   # permission_classes=[IsAuthenticated]
#   authentication_classes=[SessionAuthentication]
#   # permission_classes=[IsAuthenticated]
#   permission_classes=[IsAuthenticatedorReadOnly] 
class RouteSerializer(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = RouteSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]  # Corrected permission class
    
    #use this aythentication so need to give permission in backendadmin pannel not work from only authentication
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    







