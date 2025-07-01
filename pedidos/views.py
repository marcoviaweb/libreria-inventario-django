from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from .forms import PedidoProveedorForm, DetallePedidoProveedorFormSet
from .models import PedidoProveedor, DetallePedidoProveedor
from libros.models import Libro
from inventario.models import MovimientoInventario
from django.shortcuts import get_object_or_404
from django.db import transaction
from .forms import RecepcionDetallePedidoFormSet

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

class PedidoRecepcionView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'pedidos.change_pedidoproveedor'
    template_name = 'pedidos/pedido_recepcion.html'

    def get(self, request, pk):
        pedido = get_object_or_404(PedidoProveedor, pk=pk, estado_pedido='Pendiente')
        formset = RecepcionDetallePedidoFormSet(queryset=pedido.detalles.all())
        return render(request, self.template_name, {'pedido': pedido, 'formset': formset})

    @transaction.atomic
    def post(self, request, pk):
        pedido = get_object_or_404(PedidoProveedor, pk=pk, estado_pedido='Pendiente')
        formset = RecepcionDetallePedidoFormSet(request.POST, queryset=pedido.detalles.all())
        if formset.is_valid():
            completo = True
            for form in formset:
                detalle = form.instance
                recibida = form.cleaned_data['cantidad_recibida']
                if recibida > detalle.cantidad_pedida:
                    form.add_error('cantidad_recibida', 'No puede recibir más de lo pedido.')
                    completo = False
                if recibida < detalle.cantidad_pedida:
                    completo = False
            if not all([form.is_valid() for form in formset]):
                return render(request, self.template_name, {'pedido': pedido, 'formset': formset})
            # Procesar recepción
            for form in formset:
                detalle = form.save(commit=False)
                recibida = detalle.cantidad_recibida
                if recibida > 0:
                    # Actualizar stock
                    libro = detalle.libro
                    libro.stock_actual += recibida
                    libro.save()
                    # Registrar movimiento
                    MovimientoInventario.objects.create(
                        libro=libro,
                        tipo_movimiento='Entrada por Compra',
                        cantidad=recibida,
                        usuario=request.user,
                        referencia_origen=str(pedido.id),
                        observaciones='Recepción de pedido'
                    )
                detalle.save()
            # Actualizar estado del pedido
            if completo:
                pedido.estado_pedido = 'Completado'
            else:
                pedido.estado_pedido = 'Recibido Parcial'
            pedido.save()
            messages.success(request, 'Recepción registrada correctamente.')
            return redirect('pedido_recepcion', pk=pedido.pk)
        return render(request, self.template_name, {'pedido': pedido, 'formset': formset})

class PedidoProveedorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = PedidoProveedor
    template_name = 'pedidos/pedido_list.html'
    context_object_name = 'pedidos'
    permission_required = 'pedidos.view_pedidoproveedor'
    queryset = PedidoProveedor.objects.all().order_by('-fecha_pedido')
