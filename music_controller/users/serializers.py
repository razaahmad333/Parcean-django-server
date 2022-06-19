from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fname', 'lname', 'email', 'username', 'password','description', 'upi')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('fname', 'lname', 'email', 'username', 'password','description', 'upi')
    
class EditUserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(validators=[])
    # username  = serializers.CharField(validators=[])

    class Meta:
        model = User
        fields = ('id','fname', 'lname', 'email', 'username', 'password','description', 'upi')
    
