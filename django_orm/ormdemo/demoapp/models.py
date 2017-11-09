from datetime import datetime
from django.db import models


class Car(models.Model):

    cmake = models.CharField('Make', max_length=30)
    cmodel = models.CharField('Model', max_length=30)
    trim = models.CharField('Trim', max_length=30)
    year = models.PositiveSmallIntegerField(
        'Year',
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.year} {self.cmake} {self.cmodel} {self.trim}'
