from django.test import TestCase
from lorawan.models import Device


def populate_db_with_devices(names):

    status = ["OK", "WARNING", "ERROR"]

    for counter, name in enumerate(names):
        device = Device()
        device.DevEUI = "{:016X}".format(counter)
        device.name = name
        device.status = status[counter % 3]
        device.save()

class LoraWanTest(TestCase):

    def test_can_add_and_save_device(self):
        populate_db_with_devices(["Device 1", "Device 2", "Device 3"])

        devices = Device.objects.all()

        self.assertEqual(devices.count(), 3)
        self.assertEqual(devices[0].name, "Device 1")
        self.assertEqual(devices[1].name, "Device 2")
        self.assertEqual(devices[2].name, "Device 3")

        self.assertEqual(devices[0].status, "OK")
        self.assertEqual(devices[1].status, "WARNING")
        self.assertEqual(devices[2].status, "ERROR")

