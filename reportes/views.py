from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import F
from libros.models import Libro

class ReporteLibrosStockView(ListView):
    model = Libro
    template_name = 'reportes/reporte_libros_stock.html'
    context_object_name = 'libros'
    queryset = Libro.objects.all().order_by('titulo')

class ReporteLibrosStockBajoView(ListView):
    model = Libro
    template_name = 'reportes/reporte_libros_stock_bajo.html'
    context_object_name = 'libros'
    def get_queryset(self):
        return Libro.objects.filter(stock_actual__lte=F('stock_minimo')).order_by('titulo')

# Create your views here.
