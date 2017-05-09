from django.db import models
from django.core.validators import RegexValidator
from django.contrib.gis.db import models as gismodels

class Device(models.Model):

    # Each LoraWAN device has a 64bit unique devices ID called `DevEUI`
    # using the EUI-64 format (Extended Unique Identifier, as specified in RFC2373)
    # Note: We use a 16char hexadecimal
    DevEUI = models.CharField(
        max_length=16,
        unique = True,
        null=False,
        blank=False,
        validators = [
            RegexValidator(
                # Only allow a combinaison of 16 caps between A and F and digits. eg: 00C21B7CD84E298
                regex = "^[A-F|\d]{16}$",
                message = "Invalide EID-64. Use only 16 caps between A-F and digits. ",
            )

        ],
    )

    ERROR = "E"
    WARNING = "W"
    OK = "O"

    STATUS_CHOICES = (
        (ERROR, "ERROR"),
        (WARNING, "WARNING"),
        (OK, "OK"),
    )

    name = models.CharField(max_length=80)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
    )

    location = gismodels.PointField(null=True)
