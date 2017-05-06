#from django.contrib.gis import admin
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from lorawan import models

admin.site.register(models.Device, LeafletGeoAdmin)