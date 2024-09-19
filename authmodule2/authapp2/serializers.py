from rest_framework import serializers
from .models import *


class AllAuthSerializerData(serializers.ModelSerializer):
  class Meta:
    model=employee
    fields=['id','name','roal','domain_name','project_name']
    