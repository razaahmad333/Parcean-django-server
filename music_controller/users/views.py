from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import CreateUserSerializer, UserSerializer, EditUserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateUserView(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            fname = serializer.data.get('fname'),
            lname = serializer.data.get('lname'),
            email = serializer.data.get('email'),
            username = serializer.data.get('username'),
            password = serializer.data.get('password'),
            upi = serializer.data.get('upi'),
            description = serializer.data.get('description')   
            queryset = User.objects.filter(username=username)
            if queryset.exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                new_user = User( 
                    fname=fname,
                    lname=lname,
                    email=email,
                    username=username,
                    password=password,
                    upi=upi,
                    description=description
                )   
                new_user.save()
                print(new_user)
                return Response(UserSerializer(new_user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditUserView(APIView):
    serializer_class = EditUserSerializer
    def patch(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.data.get('fname')
            print(id)
            if id is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(id=id)
            user.fname = serializer.data.get('fname')
            user.lname = serializer.data.get('lname')
            user.email = serializer.data.get('email')
            user.username = serializer.data.get('username')
            user.password = serializer.data.get('password')
            user.upi = serializer.data.get('upi')
            user.description = serializer.data.get('description')
            user.save(update_fields=['fname', 'lname', 'email', 'username', 'password', 'upi','description'])
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)