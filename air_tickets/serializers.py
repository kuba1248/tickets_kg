from rest_framework import serializers
from .models import AirTic, Order

class AirTicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirTic
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

