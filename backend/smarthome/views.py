import paho.mqtt.client as mqtt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import HomeStatus
from .serializers import HomeStatusSerializer

LIGHT_TOGGLE_TOPIC = "light/toggle"


# Create your views here.
class HomeStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(HomeStatusSerializer(HomeStatus.objects.last()).data)

    def post(self, request):
        client = mqtt.Client()
        client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
        client.connect(
            host=settings.MQTT_SERVER,
            port=settings.MQTT_PORT,
            keepalive=settings.MQTT_KEEPALIVE,
        )
        client.publish(LIGHT_TOGGLE_TOPIC, "Do It!", 2)
