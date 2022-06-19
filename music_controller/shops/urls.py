from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import IndexView

urlpatterns = [
    path('items', IndexView.as_view(), name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)