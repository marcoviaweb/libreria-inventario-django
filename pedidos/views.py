from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from .forms import PedidoProveedorForm, DetallePedidoProveedorFormSet
from .models import PedidoProveedor, DetallePedidoProveedor
from libros.models import Libro

class PedidoProveedorCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'pedidos.add_pedidoproveedor'
    template_name = 'pedidos/pedido_form.html'

    def get(self, request):
        pedido_form = PedidoProveedorForm()
        formset = DetallePedidoProveedorFormSet()
        libros = Libro.objects.all()
        libro_costos = {str(libro.pk): float(libro.costo_adquisicion) for libro in libros}
        return render(request, self.template_name, {
            'pedido_form': pedido_form,
            'formset': formset,
            'libro_costos': libro_costos
        })

    @transaction.atomic
    def post(self, request):
        pedido_form = PedidoProveedorForm(request.POST)
        formset = DetallePedidoProveedorFormSet(request.POST)
        if pedido_form.is_valid() and formset.is_valid():
            pedido = pedido_form.save(commit=False)
            pedido.total_pedido = 0
            pedido.save()
            total = 0
            libro_cantidades = {}
            for form in formset:
                if form.cleaned_data.get('DELETE') or not form.cleaned_data:
                    continue
                libro = form.cleaned_data['libro']
                cantidad = form.cleaned_data['cantidad_pedida']
                costo_unitario = form.cleaned_data['costo_unitario_acordado']
                if libro in libro_cantidades:
                    libro_cantidades[libro]['cantidad'] += cantidad
                else:
                    libro_cantidades[libro] = {'cantidad': cantidad, 'costo': costo_unitario}
            for libro, data in libro_cantidades.items():
                DetallePedidoProveedor.objects.create(
                    pedido=pedido,
                    libro=libro,
                    cantidad_pedida=data['cantidad'],
                    costo_unitario_acordado=data['costo']
                )
                total += data['cantidad'] * float(data['costo'])
            pedido.total_pedido = total
            pedido.save()
            messages.success(request, 'Pedido creado correctamente.')
            return redirect('pedido_create')
        libros = Libro.objects.all()
        libro_costos = {str(libro.pk): float(libro.costo_adquisicion) for libro in libros}
        return render(request, self.template_name, {
            'pedido_form': pedido_form,
            'formset': formset,
            'libro_costos': libro_costos
        })
