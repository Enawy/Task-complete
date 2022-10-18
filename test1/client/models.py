from django.db import models
from car.models import Car

class Client(models.Model):
    c_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    cars_owned = models.ManyToManyField(Car)

    def __str__(self):
        return self.c_name
