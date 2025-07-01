from django.db import models

# Create your models here.

class Libro(models.Model):
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN')
    titulo = models.CharField(max_length=255, verbose_name='Título')
    autor = models.CharField(max_length=255, verbose_name='Autor(es)')
    editorial = models.CharField(max_length=255, verbose_name='Editorial')
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de Venta')
    costo_adquisicion = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Costo de Adquisición')
    stock_actual = models.IntegerField(default=0, verbose_name='Stock Actual')
    stock_minimo = models.IntegerField(default=5, verbose_name='Stock Mínimo')
    categoria = models.CharField(max_length=100, verbose_name='Categoría/Género')
    sinopsis = models.TextField(blank=True, null=True, verbose_name='Sinopsis')

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
