from django.contrib.gis import admin as geoadmin
from django.contrib import admin

from lorawan import models

class DeviceAdmin(geoadmin.OSMGeoAdmin):
    list_display = ("name", "DevEUI", "status")

class MessageAdmin(admin.ModelAdmin):
    list_display = ("device","port","datetime", "content")

admin.site.register(models.Device, DeviceAdmin)
admin.site.register(models.Message, MessageAdmin)