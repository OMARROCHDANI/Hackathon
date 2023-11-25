from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ingredients = models.TextField(max_length=255)
    preparation = models.TextField(max_length=255)
    time = models.IntegerField()  
    photo = models.ImageField(upload_to='templates/img', null=True, blank=True)

 