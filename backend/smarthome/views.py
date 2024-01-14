from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import HomeStatus
from .serializers import HomeStatusSerializer


# Create your views here.
class HomeStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(HomeStatusSerializer(HomeStatus.objects.last()).data)
