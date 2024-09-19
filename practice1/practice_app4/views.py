from django.shortcuts import render
from rest_framework.response import Response
from .models import student
from .serializers import RouteSerializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class StudentViewSets(viewsets.ViewSet):
  def list(self,request):
    queryset=student.objects.all()
    serializer=RouteSerializer(data=queryset)
    if serializer.is_valid():
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def post(self,request):
    serializer=RouteSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'data cretaed succefully'},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def get(self,request,id=None):
    if id:
      query=student.objects.get(id=id)
      serializer=RouteSerializer(data=query)
      return Response(serializer.data)
    return Response("data is not valid")
  

  def update_put(self,request,id=None):
    if id:
      query=student.objects.get(id=id)
      serializer=RouteSerializer(query,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':'data updated successfully'},status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def update_patch(self,request,id=None):
    if id:
      query=student.objects.get(id=id)
      serializer=RouteSerializer(query,data=request.data,partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':'data updated successfully'},status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
  def delete(self,request,id=None):
    if id:
      query=student.objects.get(id=id)
      serializer=RouteSerializer(data=query)
      serializer.delete()
      return Response({'msg':'data deleted successfully'},status=status.HTTP_200_OK,data={})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
