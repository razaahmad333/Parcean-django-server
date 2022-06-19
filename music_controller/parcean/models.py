from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Parcean(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name