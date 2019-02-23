from .models import vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vehicle
        fields = ('make', 'model', 'description', 'color', 'doors', 'lot_number')
