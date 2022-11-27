from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ListSensor, GetUpdateDeleteSensor, AddMeasurement, imageForm

# router = DefaultRouter()
# router.register('sensors', ListSensor.as_view())
# # router.register('sensors/<int:pk>', GetUpdateDeleteSensor.as_view())
# router.register('measurements',  AddMeasurement.as_view())
#
# urlpatterns = router.urls

urlpatterns = [
    path('sensors/', ListSensor.as_view()),
    path('sensors/<int:pk>', GetUpdateDeleteSensor.as_view()),
    path('measurements/', AddMeasurement.as_view()),
]
