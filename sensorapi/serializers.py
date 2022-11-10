from rest_framework import serializers

from . models import Sensors, Readings


class SensorsSerializer(serializers.ModelSerializer):
    # Serializer for Sensor model
    class Meta:
        model = Sensors
        fields = ('name', 'unit', 'date', 'last_modified')


class ReadingsSerializer(serializers.ModelSerializer):
    # Serializer for Readings model
    sensor_name = serializers.SerializerMethodField('get_name_from_sensors')

    class Meta:
        model = Readings
        fields = ('sensor', 'date', 'value', 'sensor_name')

    @staticmethod
    def get_name_from_sensors(sensor_id):
        sensor_name = sensor_id.sensor.name
        return sensor_name
