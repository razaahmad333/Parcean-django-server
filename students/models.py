from django.db import models
import random
import string
# Create your models here.
def getRandomPassword():
    
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

def getUserName(instance):
    return instance.user.username

class Student(models.Model):


    username = models.CharField(max_length=100, unique=True, default="")
    password = models.CharField(max_length=100, unique=True, blank=False, default="")
    Name = models.CharField(max_length=100, blank=False)
    Standard = models.CharField(max_length=20, blank=False)
    Grade = models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, blank=False)

    USERNAME_FIELD = 'username'
    is_anonymous = False
    is_authenticated = False
    REQUIRED_FIELDS = ('username', 'password',)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['Name']
