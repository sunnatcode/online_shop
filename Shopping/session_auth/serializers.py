from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.serializers import ValidationError
class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()  
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    password = serializers.CharField(max_length=200, write_only=True)

    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)

        user = User(username=username)
        user.set_password(password)
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','last_name','first_name', 'email','is_staff']

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        print(attrs)
        user = authenticate(username=attrs['username'], password=attrs['password'])

        if not user:
            raise ValidationError('Incorrect username or password')

        if not user.is_active:
            raise ValidationError('User is disabled')

        return {'user' : user}
