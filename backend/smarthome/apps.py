from django.apps import AppConfig


class SmarthomeConfig(AppConfig):
    name = "smarthome"

    def ready(self):
        from .mqtt import getMQTTClient

        client = getMQTTClient()
        client.loop_start()
