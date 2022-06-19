from django.urls import path

from .views import login, createAccount, get_me as get_parcean 

urlpatterns = [
    path('login', login),
    path('create', createAccount),
    path('me',get_parcean)
]
