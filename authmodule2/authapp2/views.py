from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .customauthentications import MyPermission

# Create your views here.

class AllAuthSerializer(viewsets.ModelViewSet):
  queryset=employee.objects.all()
  serializer_class=AllAuthSerializerData
  # authentication_classes=[SessionAuthentication]
  # permission_classes=[MyPermission]
