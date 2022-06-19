from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Parcean



class ParceanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcean
        fields = '__all__'

class LoginParceanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcean
        fields = ('username', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'