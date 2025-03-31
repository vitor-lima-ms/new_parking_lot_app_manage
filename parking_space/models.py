from django.db import models
from vehicle.models import Vehicle
from datetime import datetime, timezone

# Create your models here.

"""Model representing parking spaces"""
class ParkingSpace(models.Model):
    occupied = models.BooleanField(default=False)
    occupied_by = models.OneToOneField(
        Vehicle,
        null=True,
        default=None,
        on_delete=models.SET_NULL       
    )
    def create_list():
        return list({})

    history = models.JSONField(default=create_list, null=True)

    def __str__(self):
        return f'Vaga {self.id}'
    
    """Function to remove a veichle in a parking space"""
    def remove_auto(self):
        self.occupied = False
        self.occupied_by = None
    
    """Function to create the history of the parking space"""
    def add_history(self):
        current_datetime = datetime.now(timezone.utc)
        occupied_by = self.occupied_by
        vehicle_plate = self.occupied_by.vehicle_plate
        checkin_datetime = self.occupied_by.checkin_datetime
        total_time = current_datetime - self.occupied_by.checkin_datetime
        
        self.history.append({
            'model': str(occupied_by),
            'vehicle_plate': str(vehicle_plate),
            'checkin_datetime': str(checkin_datetime),
            'checkout_datetime': str(current_datetime),
            'total_time': str(total_time),
        })