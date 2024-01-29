import json
import paho.mqtt.client as mqtt
from django.conf import settings
from .models import HomeStatus
from .consumers import LIGHT_STATUS_TOPIC


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        mqtt_client.subscribe(LIGHT_STATUS_TOPIC)
    else:
        print("Bad connection. Code:", rc)


def on_message(mqtt_client, userdata, msg):
    print(f"Received message on topic: {msg.topic} with payload: {msg.payload}")
    if msg.topic == LIGHT_STATUS_TOPIC:
        data = json.loads(msg.payload)
        try:
            HomeStatus(on=data["on"], sent_at=data["sent_at"]).save()
        except Exception as e:
            print("Encountered error while saving data:", e)


def getMQTTClient():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
    client.connect(
        host=settings.MQTT_SERVER,
        port=settings.MQTT_PORT,
        keepalive=settings.MQTT_KEEPALIVE,
    )
    return client
