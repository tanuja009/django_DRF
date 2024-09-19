from django.db import models

# Create your models here.
class mymodel(models.Model):
  name=models.CharField(max_length=50)
  age=models.IntegerField()
  email=models.EmailField()
  contact=models.BigIntegerField()

  