from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AirTic(models.Model):
    date_arrival = models.DateTimeField(default=datetime.now)
    date_flight = models.DateTimeField(default=datetime.now)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Order(models.Model):
    pstatusy = (
        ('confirmed', 'confirmed'),
        ('reserved', 'reserved'),
        ('denied', 'denied'),
        ('returned', 'returned')
    )
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    ticket = models.ForeignKey(AirTic, related_name='orders', on_delete=models.CASCADE)
    status = models.CharField( default='reserved',
        max_length=20,
        choices=pstatusy
    )
    date_created = models.DateTimeField(blank=True, default=datetime.now)



    def __str__(self):
        return str(self.id)