from rest_framework.serializers import ModelSerializer
from .models import Question, Answer

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

