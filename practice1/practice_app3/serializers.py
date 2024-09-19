from rest_framework import serializers
from .models import *

class NewModelSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True)
  class Meta:
    model=NewModel
    fields=['id','name','email','photo']