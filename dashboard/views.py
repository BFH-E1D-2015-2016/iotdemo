from django.shortcuts import render

from lorawan.models import Device

from django.core.serializers import serialize
from django.http import HttpResponse

def dashboard(request):
    devices = Device.objects.all()
    devices_geojson = serialize('geojson', Device.objects.exclude(location__isnull=True))

    params = {
        "devices": devices,
        "devices_geojson": devices_geojson,
    }

    return render(request, 'dashboard.html', params)


