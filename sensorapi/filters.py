
from django_filters import FilterSet, AllValuesFilter, DateTimeFromToRangeFilter, RangeFilter
from . models import Readings


class ReadingsDateFilter(FilterSet):
    sensor_id = AllValuesFilter(field_name='sensor', lookup_expr='exact')
    reading_datetime = DateTimeFromToRangeFilter(field_name='date')
    sensor_values = RangeFilter(field_name='value')

    class Meta:
        model = Readings
        fields = ('sensor_id', 'reading_datetime', 'sensor_values')
