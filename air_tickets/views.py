from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import AirTic, Order
from .permissions import IsAuthor
from .serializers import AirTicSerializer, OrderSerializer
from rest_framework import viewsets


class TicketViewSet(ModelViewSet, GenericViewSet):

    queryset = AirTic.objects.all()
    serializer_class = AirTicSerializer


class OrderViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
