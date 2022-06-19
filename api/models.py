from django.db import models
import string, random

def generate_unique_code():
    length = 6
    
    while True:
        code = "".join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if not Room.objects.filter(code=code).exists():
            return code

            

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=10, default=generate_unique_code, unique=True)
    name = models.CharField(max_length=100, default="")
    host = models.CharField(max_length=100, unique=True)
    guest_can_pause = models.BooleanField(default=False, null=False)
    votes_to_skip = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    






