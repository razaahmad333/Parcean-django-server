from django.db import models
from datetime import datetime
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='items/', null=True)
    imageURL = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    parcean = models.ForeignKey('parcean.Parcean', on_delete=models.CASCADE)
    item = models.ForeignKey('shops.Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.parcean.name} ordered {str(self.quantity)} {self.item.name} for ₹{str(self.total)}'