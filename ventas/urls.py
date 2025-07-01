from django.urls import path
from .views import VentaCreateView

urlpatterns = [
    path('nueva/', VentaCreateView.as_view(), name='venta_create'),
]
