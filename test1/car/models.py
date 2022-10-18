from django.db import models
from company.models import Company

class Car(models.Model):
    model = models.CharField(max_length=50)
    model_year = models.PositiveIntegerField()
    manufacturer = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.model
