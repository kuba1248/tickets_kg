from django.contrib import admin

# Register your models here.
from .models import AirTic, Order

admin.site.register(AirTic)
admin.site.register(Order)