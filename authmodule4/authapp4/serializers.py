from rest_framework import serializers
from .models import *

class mymodelserializer(serializers.ModelSerializer):
  class Meta:
    model=mymodel
    fields=['name','age','email','contact']

    def validate_contact(self,value):
      if len(value) != 10:
        raise serializers.ValidationError("contact number be 10 digits")
      return value
    