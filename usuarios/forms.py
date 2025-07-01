from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre_rol', 'descripcion']
        widgets = {
            'nombre_rol': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_nombre_rol(self):
        nombre_rol = self.cleaned_data.get('nombre_rol')
        if self.instance.pk is None:  # Si es creación
            if Rol.objects.filter(nombre_rol__iexact=nombre_rol).exists():
                raise forms.ValidationError('Ya existe un rol con este nombre.')
        else:  # Si es edición
            if Rol.objects.filter(nombre_rol__iexact=nombre_rol).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Ya existe un rol con este nombre.')
        return nombre_rol
