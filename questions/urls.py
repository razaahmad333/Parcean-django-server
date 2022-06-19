from urllib.parse import urlparse
from django.urls import path

from .views import question_list, answer_list, submit_answer, upvote, edit_answer

urlpatterns = [
    path('questions', question_list, name='question_list'),
    path('questions/<int:question_id>/answers', answer_list, name='answer_list'),
    path('submit_answer', submit_answer, name='submit_answer'),
    path('answers/<str:answer_id>/upvote', upvote, name='vote'),
    path('answers/edit/<str:answer_id>', edit_answer, name='edit_answer'),
    path('answers/delete/<str:answer_id>', edit_answer, name='delete_answer'),
]
