from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import exceptions
from .serializers import UserRegisterSerializer, LoginSerializers, UserSerializer
from rest_framework.response import Response
from django.contrib.auth import login, logout
# Create your views here.

class SessionViewSet(ViewSet):
    permission_classes = [AllowAny,]

    def list(self, request):
        if not request.user.is_authenticated:
            raise exceptions.NotAuthenticated()
        ser = UserSerializer(request.data)
        return Response(ser.data)
    
    def create(self, request):
        serializer = LoginSerializers(request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            print(user)
            print(serializer.validated_data)
            login(request, user)
            return Response(UserSerializer(user).data, status=201)

    def destroy(self, request):
        logout(request)
        return Response(status=204)

class RegisterViewSet(ViewSet):
    permission_classes = [IsAdminUser]
    
    def create(self, request):
        serializers = UserRegisterSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=200)