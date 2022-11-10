from django.db import models

# Create your models here.
'''
Two models, Sensors and Readings, are created. 
Sensor model stores basic info on sensors such as name, unit, date created and modified.
Readings model holds the data for each sensor reading. 
Sensor model to Readings model has a one to many relationship.
'''


class Sensors(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    unit = models.CharField(max_length=50, blank=False, default='')
    date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)


class Readings(models.Model):
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    value = models.FloatField()

    class Meta:
        ordering = ('id',)
