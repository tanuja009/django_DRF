from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(NewModel)
class Newmodeladmin(admin.ModelAdmin):
  list_display=['id','name','email','photo']
