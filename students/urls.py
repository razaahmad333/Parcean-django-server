from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import index, StudentViewSet, CurrentStudent

router = DefaultRouter()
router.register('', StudentViewSet)

urlpatterns = router.urls + [
    path('current', CurrentStudent.as_view(), name='current'),
]
