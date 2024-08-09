from django.urls import path

from measurement.views import SensorsListCreateView, MeasurementCreateView, SensorChangeView, SensorView

urlpatterns = [
    path('sensors/', SensorsListCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/update/<pk>', SensorChangeView.as_view()),
    path('sensors/<pk>', SensorView.as_view())

]
