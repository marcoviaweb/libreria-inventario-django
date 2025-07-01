from django.urls import path
from .views import EntradaManualView, AjusteStockView

urlpatterns = [
    path('entrada-manual/', EntradaManualView.as_view(), name='entrada_manual'),
    path('ajuste-stock/', AjusteStockView.as_view(), name='ajuste_stock'),
]
