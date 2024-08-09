from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=300)

class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
