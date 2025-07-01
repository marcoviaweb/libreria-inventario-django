from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre_proveedor', 'contacto_principal', 'telefono', 'email')
    search_fields = ('nombre_proveedor', 'contacto_principal', 'telefono', 'email')

# Register your models here.
