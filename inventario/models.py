from django.db import models
from libros.models import Libro
from usuarios.models import Usuario

# Create your models here.

class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO_CHOICES = [
        ('Entrada por Compra', 'Entrada por Compra'),
        ('Salida por Venta', 'Salida por Venta'),
        ('Ajuste Positivo', 'Ajuste Positivo'),
        ('Ajuste Negativo', 'Ajuste Negativo'),
        ('Entrada Manual', 'Entrada Manual'),
    ]
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT, related_name='movimientos')
    tipo_movimiento = models.CharField(max_length=50, choices=TIPO_MOVIMIENTO_CHOICES)
    cantidad = models.IntegerField()
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='movimientos')
    referencia_origen = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_movimiento} - {self.libro} ({self.cantidad})"

    class Meta:
        verbose_name = 'Movimiento de Inventario'
        verbose_name_plural = 'Movimientos de Inventario'
