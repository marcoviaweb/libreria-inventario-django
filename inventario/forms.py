from django import forms
from libros.models import Libro

class EntradaManualForm(forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), label='Libro', widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(min_value=1, label='Cantidad a ingresar', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(label='Observaciones', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

class AjusteStockForm(forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), label='Libro', widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(label='Cantidad a ajustar (+/-)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(label='Razón o comentario', required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad == 0:
            raise forms.ValidationError('La cantidad no puede ser cero.')
        return cantidad
