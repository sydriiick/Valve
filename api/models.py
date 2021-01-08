from django.db import models
from datetime import datetime

class ShutdownValve(models.Model):
    id              = models.CharField(primary_key=True, max_length=50, verbose_name='ID')
    station_four    = models.FloatField(verbose_name='Station 4')
    station_five    = models.FloatField(null=True, blank=True, verbose_name='Station 5')
    station_six     = models.FloatField(null=True, blank=True, verbose_name='Station 6')
    valve           = models.FloatField(verbose_name='Shutdown Valve')
    created_on      = models.DateTimeField(auto_now_add=True,verbose_name='Created On')

    def __str__(self):
        return self.id
