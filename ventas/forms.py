from django import forms
from libros.models import Libro

class DetalleVentaForm(forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), label='Libro', widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(min_value=1, label='Cantidad', widget=forms.NumberInput(attrs={'class': 'form-control'}))

DetalleVentaFormSet = forms.formset_factory(DetalleVentaForm, extra=1, min_num=1, validate_min=True, can_delete=True)
