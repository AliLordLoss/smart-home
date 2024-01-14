from django.urls import path
from .views import HomeStatusView

urlpatterns = [
    path("status/", HomeStatusView.as_view(), name="status"),
]
