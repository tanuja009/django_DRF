from django.shortcuts import render
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from .serializers import *
from rest_framework import permissions
# Create your views here.

class LCUsersList(GenericAPIView,ListModelMixin,CreateModelMixin):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset=NewModel.objects.all()
  serializer_class=NewModelSerializer

  def get(self,request,*args,**kwargs):
    return self.list(request,*args,**kwargs)
  
  def post(self,request,*args,**kwargs):
    return self.create(request,*args,**kwargs)

class RUDUsersListUser(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset=NewModel.objects.all()
  serializer_class=NewModelSerializer
  def put(self,request,*args,**kwargs):
    return self.update(request,*args,**kwargs)
  
  def delete(self,request,*args,**kwargs):
    return self.destroy(request,*args,**kwargs)
  
  def get(self,request,*args,**kwargs):
    return self.retrieve(request,*args,**kwargs)
  

