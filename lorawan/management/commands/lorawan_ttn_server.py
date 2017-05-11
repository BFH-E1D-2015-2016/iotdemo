import json
import base64

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from lorawan.models import Device, Message

from paho.mqtt import client as mqtt_client
from paho.mqtt.client import MQTTMessage


def import_payload_data(data):
    import binascii
    from django.utils import dateparse

    dev_eui = data["hardware_serial"]
    payload = base64.b64decode(data["payload_raw"])
    port = data["port"]
    rx_time = dateparse.parse_datetime(data["metadata"]["time"])

    payload_hex = binascii.hexlify(payload)

    device, _ = Device.objects.get_or_create(
        DevEUI = dev_eui,
        defaults={
            "status": "E",
            "name": data["dev_id"],

        }
    )

    message = Message()
    message.content = payload_hex
    message.datetime = rx_time
    message.device = device
    message.port = port
    message.save()


def on_message(client: mqtt_client.Client, userdata, msg: MQTTMessage ):
   import_payload_data(json.loads(msg.payload))

def on_connect(client: mqtt_client.Client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("+/devices/+/up", qos=2)
    elif rc==3:
        # Server isn't available, retry later
        print("Server isn't available")
    else:
        # Error in config
        print("Error in config")
        client.disconnect()

def on_disconnect(client: mqtt_client.Client, userdata, rc):
    if rc != 0:
        # Network failure, try to reconnect
        client.reconnect()
    else:
        # We have called disconnect
        pass

class Command(BaseCommand):
    help = "Run TheThingsNetwork.org backend"

    def handle(self, *args, **options):
        region = settings.LORAWAN_BACKEND_TTN["REGION"]
        url = region + ".thethings.network"
        port = 8883
        username = settings.LORAWAN_BACKEND_TTN["APP_ID"]
        password = settings.LORAWAN_BACKEND_TTN["APP_ACCESS_KEY"]


        handler = mqtt_client.Client()
        handler.on_message = on_message
        handler.on_connect = on_connect
        handler.on_disconnect = on_disconnect

        handler.username_pw_set(username, password)

        #handler.tls_set()

        handler.connect(url)



        handler.loop_forever()



