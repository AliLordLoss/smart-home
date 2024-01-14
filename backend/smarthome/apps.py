from django.apps import AppConfig


class SmarthomeConfig(AppConfig):
    name = "smarthome"

    def ready(self):
        from .mqtt import client

        client.loop_start()
