from django.urls import path

from .views import login, createAccount, get_me as get_parcean, get_parcean_with_orders 

urlpatterns = [
    path('login', login),
    path('create', createAccount),
    path('me',get_parcean),
    path('meWithOrders', get_parcean_with_orders)
]
    