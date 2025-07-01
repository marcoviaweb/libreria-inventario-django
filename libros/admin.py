from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'editorial', 'precio_venta', 'stock_actual', 'stock_minimo')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('editorial', 'categoria')
