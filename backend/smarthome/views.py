import paho.mqtt.client as mqtt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import HomeStatus
from .serializers import HomeStatusSerializer, UserSerializer

LIGHT_TOGGLE_TOPIC = "light/toggle"


# Create your views here.
class HomeStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(HomeStatusSerializer(HomeStatus.objects.last()).data)

    def put(self, request):
        try:
            client = mqtt.Client()
            client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
            client.connect(host=settings.MQTT_SERVER)
            client.publish(LIGHT_TOGGLE_TOPIC, "A", 1)
            client.disconnect()
            return Response("", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserDetailsView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"error": "Refresh token is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token)
            token_data = token.payload
            user_id = token_data.get("user_id")

            if user_id != request.user.id:
                return Response(
                    {"error": "Invalid refresh token"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED
            )
