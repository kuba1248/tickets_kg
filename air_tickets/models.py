from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AirTic(models.Model):
    date_arrival = models.DateTimeField()
    date_flight = models.DateTimeField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    ticket = models.ForeignKey(AirTic, related_name='orders', on_delete=models.CASCADE)
