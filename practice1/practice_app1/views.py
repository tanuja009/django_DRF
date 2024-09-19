from django.shortcuts import render
from .models import Task
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import permissions
from django.shortcuts import get_object_or_404
# from rest_framework import permissions
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.authentication import TokenAuthentication
# from oauth2_provider.contrib.rest_framework import OAuth2Authentication

@method_decorator(csrf_exempt,name='dispatch')
class students_deatils(APIView):
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    # # authentication_classes = [OAuth2Authentication]
    

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, id=None):
        # If an ID is provided, get the specific task
        if id:
            # Use get_object_or_404 to handle the case where the task is not found
            query = get_object_or_404(Task, id=id)
            serializer = TaskSerializer(query)
            return Response({
                'data': serializer.data
            })
        queryset = Task.objects.all().order_by('-pk')
        serializer = TaskSerializer(queryset, many=True)
        return Response({
            'data': serializer.data
        })

    def post(self,request):
        data=request.data
        # serializer=TaskSerializer(data=data)
        if isinstance(data, list):  # Check if the request data is a list
            serializer = TaskSerializer(data=request.data, many=True)  # Set `many=True` for bulk creation
        else:
            serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved','data':serializer.data})
        else:
            return Response({
                'msg':'data not saved',
                'errors':serializer.errors,
            })
       
    def put(self,request):
        data=request.data
        if not data.get('id'):
           return Response({
               'message':'data is not update',
               'errors':'id is required'
           })
        details=Task.objects.get(id=data.get('id'))
        serializer=TaskSerializer(details,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'data upadate',
                'data':serializer.data
            })
        else:
            return Response({
                'msg':'data not update',
                'errors':'validation failed'

            })
       
    
    def patch(self,request):
        data=request.data
        if not data.get('id'):
            return Response({
                'message':'data not updated',
                'errors':'id is required'
            })
        details=Task.objects.get(id=data.get('id'))
        serializer=TaskSerializer(details,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'data updated',
                'data':serializer.data
            })
        else:
            return Response({
                'msg':'data is not valid',
                'errors':'data validation failed'
            })
        
    
    def delete(self,request):
        data=request.data
        if not data.get('id'):
            return Response({
                'msg':'data is not deleted',
                'errors':'id is needed'
            })
        details=Task.objects.get(id=data.get('id')).delete()
        return Response({'msg':'data id deleted','data':{}})








