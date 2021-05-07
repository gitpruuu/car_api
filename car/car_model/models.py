from django.db import models


# Create your models here.

class CarModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 30)

class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.ForeignKey(CarModel, related_name='id', on_delete=models.CASCADE)
    color = models.CharField(max_length = 30)
    year = models.DateField()
    