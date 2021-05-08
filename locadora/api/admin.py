from django.contrib import admin
from .models import CarModel, Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    search_fields = ["color", "model__name"]

admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
