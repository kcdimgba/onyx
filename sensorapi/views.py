# from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters

from . serializers import SensorsSerializer, ReadingsSerializer
from . models import Sensors, Readings
from . filters import ReadingsDateFilter

# Create your views here.


class SensorsViewSet(viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class ReadingsViewsSet(viewsets.ModelViewSet):
    queryset = Readings.objects.all()
    serializer_class = ReadingsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReadingsDateFilter
