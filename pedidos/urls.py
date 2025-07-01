from django.urls import path
from .views import PedidoProveedorCreateView

urlpatterns = [
    path('nuevo/', PedidoProveedorCreateView.as_view(), name='pedido_create'),
    # Se agregarán más vistas (listado, detalle, recepción) posteriormente
]
