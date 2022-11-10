from django.urls import include, path

from rest_framework import routers

from . views import SensorsViewSet, ReadingsViewsSet

router = routers.DefaultRouter()
router.register(r'api/sensors', SensorsViewSet)
router.register(r'api/data', ReadingsViewsSet)

urlpatterns = [
    path('', include(router.urls)),
]
