from rest_framework import serializers
from .models import HomeStatus


class HomeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStatus
        fields = "__all__"
