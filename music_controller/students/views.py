from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import StudentSerializer
from .models import Student
from .helpers import queryset_to_dict

def index(request):
    # students = list(Student.objects.values())
    students = queryset_to_dict(Student.objects.all())
    
    return JsonResponse(students, safe=False)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class CurrentStudent(APIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)