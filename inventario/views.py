from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .forms import EntradaManualForm
from .models import MovimientoInventario
from libros.models import Libro

class EntradaManualView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    template_name = 'inventario/entrada_manual.html'
    form_class = EntradaManualForm
    success_url = reverse_lazy('entrada_manual')
    permission_required = 'inventario.add_movimientoinventario'

    def form_valid(self, form):
        libro = form.cleaned_data['libro']
        cantidad = form.cleaned_data['cantidad']
        observaciones = form.cleaned_data['observaciones']
        usuario = self.request.user
        # Actualizar stock
        libro.stock_actual += cantidad
        libro.save()
        # Registrar movimiento
        MovimientoInventario.objects.create(
            libro=libro,
            tipo_movimiento='Entrada Manual',
            cantidad=cantidad,
            usuario=usuario,
            observaciones=observaciones
        )
        messages.success(self.request, f'Se registró la entrada de {cantidad} unidades para "{libro}".')
        return super().form_valid(form)

# Create your views here.
