from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Rol, Usuario

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

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'nombre_completo', 'email', 'rol', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class UsuarioChangeForm(UserChangeForm):
    password = None  # Oculta el campo password en el formulario de edición
    class Meta:
        model = Usuario
        fields = ('username', 'nombre_completo', 'email', 'rol', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
