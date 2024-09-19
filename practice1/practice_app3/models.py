from django.db import models

# Create your models here.
class NewModel(models.Model):
  name=models.CharField(max_length=50)
  email=models.EmailField()
  photo=models.ImageField(upload_to="profile_image")
