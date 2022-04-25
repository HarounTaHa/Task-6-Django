from django.db import models


# Create your models here.


class Vendor(models.Model):
    mac = models.CharField(max_length=6)
    vendor = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.mac},{self.vendor}'
