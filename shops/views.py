from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Item, Order
from .serializers import ItemSerializer, Order

from parcean.models import Parcean
from parcean.serializers import ParceanSerializer

from rest_framework.permissions import IsAuthenticated

class IndexView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('errors', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetItemById(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        item = Item.objects.get(id=id)
        item_serializer = ItemSerializer(item)
        print(id)
        return Response(item_serializer.data, status=status.HTTP_200_OK)

class BuyItem(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        user = request.user

        item = Item.objects.get(id=request.data['item'])
        quantity = int(request.data['quantity'])
        total = int(request.data['total'])

        parcean = Parcean.objects.get(user=user)
        order = Order(item=item, parcean=parcean, quantity=quantity,  total=total)
        order.save()
        parcean.wallet -= total
        parcean.save()

        return Response(ParceanSerializer(parcean).data,status=status.HTTP_200_OK)


