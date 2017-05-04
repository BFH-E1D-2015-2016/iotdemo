from django.shortcuts import render

from dashboard.models import Device

def dashboard(request):
    devices = Device.objects.all()

    params = {
        "devices": devices
    }

    return render(request, 'dashboard.html', params)
