from django.db import models

class Company(models.Model):
    com_name = models.CharField(max_length=50)

    def __str__(self):
        return self.com_name
