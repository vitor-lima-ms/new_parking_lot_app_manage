from django.contrib import admin
from vehicle.models import Vehicle

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'model',
        'vehicle_plate',
        'checkin_datetime',
    ]

    class Meta:
        ordering = (('-checkin_datetime',))
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'