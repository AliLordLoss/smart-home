from django.urls import path
from .views import HomeStatusView

urlpatterns = [
    path("home-light/", HomeStatusView.as_view(), name="home-light"),
]
