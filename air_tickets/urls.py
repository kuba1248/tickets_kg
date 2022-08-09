from django.urls import path, include

from .views import TicketViewSet, OrderViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('orders', OrderViewSet, basename='orders')
router.register('', TicketViewSet, basename='tickets')

urlpatterns = [
    path('', include(router.urls)),
]
