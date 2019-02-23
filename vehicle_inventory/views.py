# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import vehicle
from rest_framework import viewsets
from serializers import VehicleSerializer

# Create your views here.
def index(request):
    cars = vehicle.objects.all()
    print(cars)
    return render(request, 'index.html', locals())

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = vehicle.objects.all()
    serializer_class = VehicleSerializer
