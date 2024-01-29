"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from smarthome.consumers import HomeStatusConsumer
from .middlewares import TokenAuthMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

websocket_urlpatterns = [path("ws/home-light/", (HomeStatusConsumer.as_asgi()))]

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": (URLRouter(websocket_urlpatterns)),
    }
)
