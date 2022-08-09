from rest_framework import serializers
from .models import AirTic, Order

class AirTicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirTic
        fields = '__all__' 

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_["orders"] = instance.orders.all().count()
        dict_["orderdet"] = OrderSerializer(instance.orders.all(),many=True).data
        return dict_
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    