from django.urls import path, include
from .views import RoomView, CreateRoomView, UserViewSet, GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet);
router.register(r'groups', GroupViewSet);

urlpatterns = [
     path('room',RoomView.as_view()),
     path('create-room', CreateRoomView.as_view()),
     path('', include(router.urls)),
]
# urlpatterns = router.urls;