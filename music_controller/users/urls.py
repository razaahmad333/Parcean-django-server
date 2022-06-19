from django.urls import path

from .views import CreateUserView, UserView, UserListView, EditUserView

urlpatterns = [
    path('create', CreateUserView.as_view()),
    path('list',UserListView.as_view()),
    path('<int:id>', UserView.as_view()),   
    path('edit', EditUserView.as_view())
]
