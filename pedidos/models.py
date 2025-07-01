from django.db import models
from proveedores.models import Proveedor
from libros.models import Libro

class PedidoProveedor(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Enviado', 'Enviado'),
        ('Recibido Parcial', 'Recibido Parcial'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado'),
    ]
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, related_name='pedidos')
    fecha_pedido = models.DateField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Pendiente')
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido #{self.id} a {self.proveedor} ({self.estado_pedido})"

class DetallePedidoProveedor(models.Model):
    pedido = models.ForeignKey(PedidoProveedor, on_delete=models.CASCADE, related_name='detalles')
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT)
    cantidad_pedida = models.IntegerField()
    cantidad_recibida = models.IntegerField(default=0)
    costo_unitario_acordado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.libro} x {self.cantidad_pedida} (Pedido #{self.pedido.id})"
