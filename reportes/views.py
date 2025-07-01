from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import F
from libros.models import Libro
from inventario.models import MovimientoInventario
from django.utils import timezone
from django import forms
from ventas.models import Venta, DetalleVenta

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

class FiltroMovimientosForm(forms.Form):
    tipo = forms.ChoiceField(
        choices=[('', 'Todos')] + MovimientoInventario.TIPO_MOVIMIENTO_CHOICES,
        required=False,
        label='Tipo de Movimiento',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    fecha_inicio = forms.DateField(required=False, label='Desde', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    fecha_fin = forms.DateField(required=False, label='Hasta', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

class ReporteMovimientosInventarioView(ListView):
    model = MovimientoInventario
    template_name = 'reportes/reporte_movimientos_inventario.html'
    context_object_name = 'movimientos'
    paginate_by = 30

    def get_queryset(self):
        qs = MovimientoInventario.objects.select_related('libro', 'usuario').order_by('-fecha_movimiento')
        tipo = self.request.GET.get('tipo')
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')
        if tipo:
            qs = qs.filter(tipo_movimiento=tipo)
        if fecha_inicio:
            qs = qs.filter(fecha_movimiento__date__gte=fecha_inicio)
        if fecha_fin:
            qs = qs.filter(fecha_movimiento__date__lte=fecha_fin)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro_form'] = FiltroMovimientosForm(self.request.GET)
        return context

class FiltroVentasForm(forms.Form):
    fecha_inicio = forms.DateField(required=False, label='Desde', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    fecha_fin = forms.DateField(required=False, label='Hasta', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), required=False, label='Libro', widget=forms.Select(attrs={'class': 'form-select'}))

class ReporteVentasView(ListView):
    model = Venta
    template_name = 'reportes/reporte_ventas.html'
    context_object_name = 'ventas'
    paginate_by = 30

    def get_queryset(self):
        qs = Venta.objects.prefetch_related('detalles__libro', 'usuario').order_by('-fecha_venta')
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')
        libro_id = self.request.GET.get('libro')
        if fecha_inicio:
            qs = qs.filter(fecha_venta__date__gte=fecha_inicio)
        if fecha_fin:
            qs = qs.filter(fecha_venta__date__lte=fecha_fin)
        if libro_id:
            qs = qs.filter(detalles__libro_id=libro_id).distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro_form'] = FiltroVentasForm(self.request.GET)
        return context

# Create your views here.
