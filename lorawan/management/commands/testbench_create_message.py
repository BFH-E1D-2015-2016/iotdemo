import base64

from django.core.management.base import BaseCommand
from lorawan.models import Device, Message
import json

class Command(BaseCommand):

    help = "Testbench for creating and saving message"

    def handle(self, *args, **options):
        for i in range(1000):
            a = json.loads("""{"app_id":"my-app-id","dev_id":"my-dev-id","hardware_serial":"0102030405060708","port":1,"counter":2,"is_retry":false,"confirmed":false,"payload_raw":"AQIDBA==","payload_fields":{},"metadata":{"time":"1970-01-01T00:00:00Z","frequency":868.1,"modulation":"LORA","data_rate":"SF7BW125","coding_rate":"4/5","gateways":[{"gtw_id":"ttn-herengracht-ams","timestamp":12345,"time":"1970-01-01T00:00:00Z","channel":0,"rssi":-25,"snr":5,"rf_chain":0,"latitude":52.1234,"longitude":6.1234,"altitude":6}],"latitude":52.2345,"longitude":6.2345,"altitude":2}}""")
            self.load_json(a)

    def load_json(self, data):
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




