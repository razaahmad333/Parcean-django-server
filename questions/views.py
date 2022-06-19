from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from students.models import Student
from students.serializers import StudentSerializer
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from parcean.serializers import ParceanSerializer
from parcean.models import Parcean

@api_view(['GET'])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        question_dict = []
        for q in questions:
            answers = Answer.objects.filter(question_id=q.id)
            question_serializer = QuestionSerializer(q)
            answer_dict = []

            for answer in answers:

                parcean = Parcean.objects.get(id=answer.given_by_id)
                parcean_serializer  = ParceanSerializer(parcean)
                answer_dict.append(
                    {
                        'id': answer.id,
                        'text': answer.answer_text,
                        'votes': answer.votes,
                        'given_by': parcean_serializer.data,
                        'created_at': answer.created_at,
                        'updated_at': answer.updated_at
                    }
                )

            question_dict.append(
                {
                    "question":question_serializer.data,
                    "answers":answer_dict
                }
            )
        return Response(question_dict)


def answer_list(request, question_id):
    if request.method == 'GET':
        answers = Answer.objects.filter(question_id=question_id)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def submit_answer(request):
    if request.method == 'POST':
        data = request.data
        user = request.user
        parcean = Parcean.objects.get(user=user)
        question_id = data['question']
        answer_text = data['text']
        given_by_id = parcean.id
        answer = Answer(
            question_id=question_id,
            answer_text=answer_text,
            given_by_id=given_by_id,
        )
        answer.save()
        return Response({'status': 'ok'})
        
@api_view(["GET", "POST"])
def upvote(request, answer_id):
    if request.method == 'POST':
        answer = Answer.objects.get(id=answer_id)
        answer.votes += 1
        answer.save(update_fields=['votes'])
        return Response({'status': 'ok'})


@api_view(["POST", "DELETE"])
@permission_classes((IsAuthenticated,))
def edit_answer(request, answer_id):
    if request.method == 'POST':
        data = request.data
        user = request.user
        parcean = Parcean.objects.get(user=user)
        answer = Answer.objects.get(id=answer_id)
        if answer.given_by_id == parcean.id:
            answer.answer_text = data['text']
            answer.updated_at = timezone.now()
            answer.save(update_fields=['answer_text', 'updated_at'])
            return Response({'status': 'ok'}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'DELETE':
        answer = Answer.objects.get(id=answer_id)
        answer.delete()
        return Response({},status=status.HTTP_200_OK)
