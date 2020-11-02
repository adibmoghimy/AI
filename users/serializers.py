from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm

class UserSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, use_url=True)
    class Meta: 
        model = User
        fields= ['username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user