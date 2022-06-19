from django.db import models
import datetime
from django.utils import timezone
from students.models import Student
from parcean.models import Parcean

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Question")
    pub_date = models.DateField(verbose_name='date published', default=timezone.now) 
    created_at = models.DateTimeField( default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    # answers = models.ForeignKey('Answer', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=200, verbose_name="Answer")
    votes = models.IntegerField(default=0, verbose_name="Votes")
    given_by = models.ForeignKey(Parcean, on_delete=models.CASCADE)
    created_at = models.DateTimeField( default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.answer_text
