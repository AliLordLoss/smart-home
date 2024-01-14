from rest_framework import serializers
from .models import HomeStatus
from django.contrib.auth.models import User


class HomeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStatus
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
