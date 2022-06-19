from operator import mod
from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=100, default="")
    lname = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100, default="")
    upi = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

