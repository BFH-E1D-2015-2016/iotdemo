from django.shortcuts import render

from lorawan.models import Device

from django.core.serializers import serialize
from django.http import HttpResponse

def dashboard(request):
    devices = Device.objects.all()

    params = {
        "devices": devices
    }

    return render(request, 'dashboard.html', params)

def devices_location(request):
    geojson = serialize('geojson', Device.objects.exclude(location__isnull=True))

    return HttpResponse(geojson, content_type='json')

