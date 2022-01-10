from rest_framework import fields, serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']