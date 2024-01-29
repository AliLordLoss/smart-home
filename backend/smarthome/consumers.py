from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from aiomqtt import Client


LIGHT_STATUS_TOPIC = "light/status"


class HomeStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope["user"]

        if not user.is_authenticated:
            try:
                print("ws: received connection, waiting for accept...")
                await self.accept("notif")
                print("ws: connection accepted. creating mqtt client...")
                await self.connect_mqtt()
            except Exception as e:
                print("FUCK:", e)

    async def connect_mqtt(self):
        async with Client(
            settings.MQTT_SERVER,
            username=settings.MQTT_USER,
            password=settings.MQTT_PASSWORD,
        ) as client:
            print("ws: Connected successfully")
            await client.subscribe(LIGHT_STATUS_TOPIC)
            async for msg in client.messages:
                data = msg.payload.decode()
                print("ws: received message:", data)
                print("ws: sending it through ws...")
                await self.send(text_data=data)
                print("ws: data sent to client.")

    async def disconnect(self, code):
        print("disconnecting")
        return await super().disconnect(code)
