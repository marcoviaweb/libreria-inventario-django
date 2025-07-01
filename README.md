# Sistema de Gestión de Inventario para Librería

Este proyecto es un sistema web desarrollado en Django para la gestión de inventario, ventas, proveedores y reportes en una librería.

## Características principales
- Gestión de roles y usuarios con permisos.
- Registro, edición y búsqueda de libros.
- Control de stock: ingresos, ajustes y movimientos de inventario.
- Registro de ventas y actualización automática de stock.
- Gestión de proveedores y pedidos a proveedores.
- Recepción de pedidos y actualización de inventario.
- Reportes de stock, ventas y movimientos.
- Interfaz moderna con Bootstrap y menú lateral.
- Autenticación y control de acceso por roles.

## Instalación y ejecución
1. Clona el repositorio y entra al directorio del proyecto.
2. Instala las dependencias necesarias:
   ```
   pip install django
   ```
3. Aplica las migraciones:
   ```
   python manage.py migrate
   ```
4. Crea un superusuario:
   ```
   python manage.py createsuperuser
   ```
5. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```
6. Accede a la aplicación en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Estructura del proyecto
- `usuarios/`: Gestión de roles y usuarios.
- `libros/`: Gestión de libros.
- `inventario/`: Movimientos y control de stock.
- `ventas/`: Registro de ventas.
- `proveedores/`: Gestión de proveedores.
- `pedidos/`: Pedidos a proveedores y recepción.
- `reportes/`: Reportes de inventario y ventas.
- `templates/`: Plantillas base y de login.

## Seguridad
- Todas las vistas principales requieren autenticación.
- El acceso a funcionalidades está protegido por permisos y roles.

## Notas
- El sistema está pensado para uso interno de librerías.
- Para más detalles, revisa los archivos `PROJECT_SPEC.md` y `DATABASE_MODEL.md`.

---
Desarrollado con Django 5.x
