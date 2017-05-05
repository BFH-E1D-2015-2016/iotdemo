from django.test import TestCase
from lorawan.models import Device


def populate_db_with_devices(names):


    for counter, name in enumerate(names):
        device = Device()
        device.DevEUI = "{:016X}".format(counter)
        device.name = name
        device.save()

class LoraWanTest(TestCase):

    def test_can_add_and_save_device(self):
        populate_db_with_devices(["Device 1", "Device 2"])

        devices = Device.objects.all()

        assert devices.count() == 2
        assert devices[0].name == "Device 1"
        assert devices[1].name == "Device 2"