from rest_framework.serializers import ModelSerializer

from .models import Item, Order

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

        