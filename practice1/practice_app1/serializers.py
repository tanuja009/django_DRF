from rest_framework import serializers
from rest_framework.views import APIView
from .models import *
# class TaskSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=100)

class TaskSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
    def length_name(value):
        if not len(value)>=5:
            raise serializers.ValidationError("name must be length 5 or greater")
    name=serializers.CharField(validators=[length_name])
    class Meta:
        model=Task
        fields=['name','roll','city']
        read_only=['name','roll']

    def validate_city(self,value):
        if value.lower() != "indore":
            raise serializers.ValidationError("city is not matched according to our condition")
        return value
    
    def validate(self, data):
        name = data.get('name')  # Correct way to get 'name' from data
        roll=data.get('roll')
        if not name.startswith('r'):  # Correct usage of startswith() method
            raise serializers.ValidationError("Name must start with 'r'")
        elif not roll > 100:
            raise serializers.ValidationError("roll no is must be greater than 100")
        return data


        
        
# class ClassSerializer(serializers.Serializer):
#     class_name=serializers.CharField(max_length=50)
#     section=serializers.CharField(max_length=50)
#     url=serializers.URLField(allow_blank=True,required=False)

     