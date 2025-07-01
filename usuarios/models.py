from django.db import models
from django.contrib.auth.models import AbstractUser

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

class Usuario(AbstractUser):
    nombre_completo = models.CharField(max_length=150, verbose_name='Nombre completo')
    email = models.EmailField(unique=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, related_name='usuarios', verbose_name='Rol')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
