from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(mymodel)
class mymodeladmin(admin.ModelAdmin):
  list_display=['id','name','age','email','contact']
  