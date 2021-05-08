from django.db import models


# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=30)
    creation_date = models.DateField(auto_now_add=True, null= True, blank=True)

    def __str__(self):
        # return 'Model %s Created at %s' % (self.name, str(self.creation_date))
        return f'Model {self.name} Created at {self.creation_date}'


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(max_length=30)
    year = models.DateField()
