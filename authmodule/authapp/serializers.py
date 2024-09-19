from rest_framework import serializers
from .models import *


class RouteSerializer(serializers.ModelSerializer):
  class Meta:
    model=student
    fields=['id','name','roll','city']
    