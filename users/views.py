from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm

class Register(CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(f"The user with {user.username} user name created succesfully", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)