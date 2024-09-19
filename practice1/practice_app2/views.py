from django.shortcuts import render
from .models import student
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import permissions
from django.contrib.auth import views as auth_views
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.authentication import TokenAuthentication
# from oauth2_provider.contrib.rest_framework import OAuth2Authentication

@method_decorator(csrf_exempt,name='dispatch')
class students_details(APIView):
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    # # authentication_classes = [OAuth2Authentication]
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, id=None):
        # If an ID is provided, get the specific task
        if id:
            # Use get_object_or_404 to handle the case where the task is not found
            query = get_object_or_404(student, id=id)
            serializer = StudentSerializer(query)
            return Response({
                'data': serializer.data
            })
        queryset = student.objects.all().order_by('-pk')
        serializer = StudentSerializer(queryset, many=True)
        return Response({
            'data': serializer.data
        })
    
    def post(self,request):
        data=request.data
        # serializer=TaskSerializer(data=data)
        if isinstance(data, list):  # Check if the request data is a list
            serializer = StudentSerializer(data=request.data, many=True)  # Set `many=True` for bulk creation
        else:
            serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved','data':serializer.data})
        else:
            return Response({
                'msg':'data not saved',
                'errors':serializer.errors,
            })
