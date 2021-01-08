from rest_framework import serializers
from .models import ShutdownValve

class ShutdownValveSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShutdownValve
        fields = ('id','station_four','valve')