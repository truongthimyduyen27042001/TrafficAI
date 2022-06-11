from django.db import models

# Create your models here.

# class Camera(models.Model):
#     camera = models.TextField(max_length=255)
#     address = models.TextField(max_length=255)


# class VehicleType(models.Model):
#     type = models.TextField(max_length=255)


class VehicleSpeed(models.Model):
    date = models.DateField(default=True)
    time = models.TimeField(default=True)
    camera = models.CharField(max_length=20)
    speed = models.FloatField()
    number_plate = models.TextField(max_length=20,default=True)
    vehicle_type = models.CharField(max_length=50)

    def hour(self):
        return self.time.hour


# class MyFile(models.Model):
#     file = models.FileField(blank=False, null=False)

    