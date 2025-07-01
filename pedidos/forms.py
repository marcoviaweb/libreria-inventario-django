from django import forms
from .models import PedidoProveedor, DetallePedidoProveedor
from proveedores.models import Proveedor
from libros.models import Libro

class PedidoProveedorForm(forms.ModelForm):
    class Meta:
        model = PedidoProveedor
        fields = ['proveedor']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }

class DetallePedidoProveedorForm(forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), label='Libro', widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad_pedida = forms.IntegerField(min_value=1, label='Cantidad Pedida', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    costo_unitario_acordado = forms.DecimalField(min_value=0, decimal_places=2, max_digits=10, label='Costo Unitario', widget=forms.NumberInput(attrs={'class': 'form-control'}))

DetallePedidoProveedorFormSet = forms.formset_factory(DetallePedidoProveedorForm, extra=1, min_num=1, validate_min=True, can_delete=True)

class RecepcionDetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedidoProveedor
        fields = ['cantidad_recibida']
        widgets = {
            'cantidad_recibida': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }

RecepcionDetallePedidoFormSet = forms.modelformset_factory(
    DetallePedidoProveedor,
    form=RecepcionDetallePedidoForm,
    extra=0,
)
