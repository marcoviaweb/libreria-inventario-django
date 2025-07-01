from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=255, unique=True)
    contacto_principal = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre_proveedor
