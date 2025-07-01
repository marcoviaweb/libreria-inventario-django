from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'titulo', 'autor', 'editorial', 'precio_venta', 'costo_adquisicion', 'categoria', 'sinopsis']
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'costo_adquisicion': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if Libro.objects.filter(isbn=isbn).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un libro con este ISBN.')
        return isbn
