from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import IndexView, GetItemById, BuyItem

urlpatterns = [
    path('items', IndexView.as_view(), name='index'),
    path('items/<str:id>',GetItemById.as_view(), name='getItemById'),
    path('orders', BuyItem.as_view(), name='buyItem'),
]

urlpatterns = format_suffix_patterns(urlpatterns)