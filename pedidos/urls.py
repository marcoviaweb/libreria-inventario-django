from django.urls import path
from .views import PedidoProveedorCreateView, PedidoRecepcionView, PedidoProveedorListView

urlpatterns = [
    path('', PedidoProveedorListView.as_view(), name='pedido_list'),
    path('nuevo/', PedidoProveedorCreateView.as_view(), name='pedido_create'),
    path('<int:pk>/recepcion/', PedidoRecepcionView.as_view(), name='pedido_recepcion'),
    # Se agregarán más vistas (listado, detalle, recepción) posteriormente
]
