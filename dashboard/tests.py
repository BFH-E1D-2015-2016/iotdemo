import pytest

from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from dashboard.views import dashboard
from dashboard.models import Device

def populate_db_with_devices(names):

    for name in names:
        device = Device()
        device.name = name
        device.save()

@pytest.mark.django_db
def test_root_url_resolves_to_dashboard_view():
    found = resolve("/")
    assert found.func == dashboard

@pytest.mark.django_db
def test_root_url_use_dashboard_template(client):
    response = client.get("/")
    html = response.content.decode("utf8")

    expected_html = render_to_string('dashboard.html')
    assert html == expected_html

@pytest.mark.django_db
def test_can_add_and_save_device():
    populate_db_with_devices(["Device 1", "Device 2"])

    devices = Device.objects.all()

    assert devices.count() == 2
    assert devices[0].name == "Device 1"
    assert devices[1].name == "Device 2"




