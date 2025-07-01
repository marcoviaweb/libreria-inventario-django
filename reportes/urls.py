from django.urls import path
from .views import ReporteLibrosStockView, ReporteLibrosStockBajoView, ReporteMovimientosInventarioView

urlpatterns = [
    path('libros-stock/', ReporteLibrosStockView.as_view(), name='reporte_libros_stock'),
    path('libros-stock-bajo/', ReporteLibrosStockBajoView.as_view(), name='reporte_libros_stock_bajo'),
    path('movimientos-inventario/', ReporteMovimientosInventarioView.as_view(), name='reporte_movimientos_inventario'),
]
