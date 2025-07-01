from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=100, unique=True, verbose_name='Nombre del Rol')
    descripcion = models.TextField(verbose_name='Descripción')

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre_rol

    def can_delete(self):
        """Verifica si el rol puede ser eliminado"""
        return not self.usuarios_set.exists()
