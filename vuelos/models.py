from django.db import models

class flight(models.Model):
    NATIONAL = 'Nacional'
    INTERNATIONAL = 'Internacional'
    
    FLIGHT_TYPES = [
        (NATIONAL, 'Nacional'),
        (INTERNATIONAL, 'Internacional'),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    flight_type = models.CharField(max_length=15, choices=FLIGHT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.name} ({self.flight_type})'