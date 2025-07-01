from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .forms import DetalleVentaFormSet
from .models import Venta, DetalleVenta
from inventario.models import MovimientoInventario
from libros.models import Libro
from django.db import transaction

class VentaCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'ventas.add_venta'
    template_name = 'ventas/venta_form.html'

    def get(self, request):
        formset = DetalleVentaFormSet()
        # Obtener todos los libros y sus precios para el JS del template
        libros = Libro.objects.all()
        libro_precios = {str(libro.pk): float(libro.precio_venta) for libro in libros}
        return render(request, self.template_name, {'formset': formset, 'libro_precios': libro_precios})

    @transaction.atomic
    def post(self, request):
        formset = DetalleVentaFormSet(request.POST)
        if formset.is_valid():
            venta = Venta.objects.create(usuario=request.user, total=0)
            total = 0
            libro_cantidades = {}
            for form in formset:
                if form.cleaned_data.get('DELETE') or not form.cleaned_data:
                    continue
                libro = form.cleaned_data['libro']
                cantidad = form.cleaned_data['cantidad']
                if libro in libro_cantidades:
                    libro_cantidades[libro] += cantidad
                else:
                    libro_cantidades[libro] = cantidad
            # Validar stock antes de registrar la venta
            for libro, cantidad in libro_cantidades.items():
                if libro.stock_actual < cantidad:
                    messages.error(request, f'Stock insuficiente para {libro}.')
                    transaction.set_rollback(True)
                    return render(request, self.template_name, {'formset': formset})
            # Registrar detalles y movimientos
            for libro, cantidad in libro_cantidades.items():
                precio_unitario = libro.precio_venta
                subtotal = precio_unitario * cantidad
                DetalleVenta.objects.create(
                    venta=venta,
                    libro=libro,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    subtotal=subtotal
                )
                libro.stock_actual -= cantidad
                libro.save()
                MovimientoInventario.objects.create(
                    libro=libro,
                    tipo_movimiento='Salida por Venta',
                    cantidad=-cantidad,
                    usuario=request.user,
                    referencia_origen=str(venta.id),
                    observaciones='Venta registrada'
                )
                total += subtotal
            venta.total = total
            venta.save()
            messages.success(request, f'Venta registrada correctamente. Total: ${total:.2f}')
            return redirect('venta_create')
        return render(request, self.template_name, {'formset': formset})
