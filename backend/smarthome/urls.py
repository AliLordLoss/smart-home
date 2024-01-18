from django.urls import path
from .views import HomeStatusView, UserDetailsView, LogoutView

urlpatterns = [
    path("home-light/", HomeStatusView.as_view(), name="home-light"),
    path("user/", UserDetailsView.as_view(), name="user"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
