from django.contrib.gis import admin
from lorawan import models

admin.site.register(models.Device, admin.OSMGeoAdmin)