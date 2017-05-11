#from django.contrib.gis import admin
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from lorawan import models

class DeviceAdmin(LeafletGeoAdmin):
    list_display = ("name", "DevEUI", "status")

class MessageAdmin(admin.ModelAdmin):
    list_display = ("device","port","datetime", "content")

admin.site.register(models.Device, DeviceAdmin)
admin.site.register(models.Message, MessageAdmin)