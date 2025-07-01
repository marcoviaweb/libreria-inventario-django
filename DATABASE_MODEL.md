# Modelo Relacional del Sistema de Inventario de Librería

Este documento detalla las tablas de la base de datos (entidades), sus atributos y las relaciones entre ellas. Se utilizarán los tipos de campo de Django correspondientes.

## 1. Entidades (Tablas) y sus Atributos

### 1.1. Usuarios
**Descripción:** Almacena la información de los empleados que acceden al sistema.
* **id_usuario** (PK, `AutoField` en Django): Identificador único del usuario.
* **nombre_usuario** (`CharField`, `unique=True`): Nombre de usuario para iniciar sesión.
* **password** (`CharField`): Contraseña hasheada (Django gestiona esto).
* **nombre_completo** (`CharField`): Nombre completo del empleado.
* **email** (`EmailField`): Correo electrónico del empleado.
* **id_rol** (FK, `ForeignKey` a `Roles`): Referencia al rol asignado al usuario.

### 1.2. Roles
**Descripción:** Define los diferentes niveles de permisos dentro del sistema.
* **id_rol** (PK, `AutoField` en Django): Identificador único del rol.
* **nombre_rol** (`CharField`, `unique=True`): Nombre del rol (ej. 'Administrador', 'Encargado de Inventario', 'Vendedor/Cajero').
* **descripcion** (`TextField`): Breve descripción de las funciones del rol.

### 1.3. Libros
**Descripción:** Contiene los detalles de cada título disponible en la librería.
* **id_libro** (PK, `AutoField` en Django): Identificador único del libro.
* **isbn** (`CharField`, `unique=True`, `max_length=13`): International Standard Book Number.
* **titulo** (`CharField`): Título del libro.
* **autor** (`CharField`): Nombre del autor o autores.
* **editorial** (`CharField`): Editorial que publicó el libro.
* **precio_venta** (`DecimalField`, `max_digits=10`, `decimal_places=2`): Precio de venta al público.
* **costo_adquisicion** (`DecimalField`, `max_digits=10`, `decimal_places=2`): Costo de compra del libro.
* **stock_actual** (`IntegerField`, `default=0`): Cantidad de ejemplares disponibles.
* **stock_minimo** (`IntegerField`, `default=5`): Cantidad mínima para activar alerta.
* **categoria** (`CharField`): Género o categoría del libro.
* **sinopsis** (`TextField`, `blank=True`, `null=True`): Descripción o sinopsis del libro.

### 1.4. Proveedores
**Descripción:** Almacena la información de contacto de las distribuidoras o editoriales.
* **id_proveedor** (PK, `AutoField` en Django): Identificador único del proveedor.
* **nombre_proveedor** (`CharField`): Nombre de la empresa proveedora.
* **contacto_principal** (`CharField`, `blank=True`, `null=True`): Nombre de la persona de contacto.
* **telefono** (`CharField`, `blank=True`, `null=True`): Número de teléfono del proveedor.
* **email** (`EmailField`, `blank=True`, `null=True`): Correo electrónico del proveedor.

### 1.5. Pedidos_Proveedores
**Descripción:** Registra cada orden de compra realizada a un proveedor.
* **id_pedido** (PK, `AutoField` en Django): Identificador único del pedido.
* **proveedor** (FK, `ForeignKey` a `Proveedores`): Referencia al proveedor.
* **fecha_pedido** (`DateField`, `auto_now_add=True`): Fecha en que se generó el pedido.
* **estado_pedido** (`CharField`, `max_length=50`, `default='Pendiente'`, `choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Recibido Parcial', 'Recibido Parcial'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')]`): Estado actual del pedido.
* **total_pedido** (`DecimalField`, `max_digits=10`, `decimal_places=2`, `default=0.00`): Suma total del valor del pedido.

### 1.6. Detalle_Pedido_Proveedor
**Descripción:** Contiene los libros incluidos en cada pedido a proveedor y sus cantidades.
* **id_detalle_pedido** (PK, `AutoField` en Django): Identificador único del detalle.
* **pedido** (FK, `ForeignKey` a `Pedidos_Proveedores`): Referencia al pedido.
* **libro** (FK, `ForeignKey` a `Libros`): Referencia al libro específico.
* **cantidad_pedida** (`IntegerField`): Cantidad de ejemplares de este libro solicitados.
* **cantidad_recibida** (`IntegerField`, `default=0`): Cantidad de ejemplares realmente recibidos.
* **costo_unitario_acordado** (`DecimalField`, `max_digits=10`, `decimal_places=2`): Costo por unidad acordado.

### 1.7. Movimientos_Inventario
**Descripción:** Registra cada cambio en el stock de un libro (entradas, salidas, ajustes).
* **id_movimiento** (PK, `AutoField` en Django): Identificador único del movimiento.
* **libro** (FK, `ForeignKey` a `Libros`): Referencia al libro afectado.
* **tipo_movimiento** (`CharField`, `max_length=50`, `choices=[('Entrada por Compra', 'Entrada por Compra'), ('Salida por Venta', 'Salida por Venta'), ('Ajuste Positivo', 'Ajuste Positivo'), ('Ajuste Negativo', 'Ajuste Negativo'), ('Entrada Manual', 'Entrada Manual')]`): Tipo de movimiento.
* **cantidad** (`IntegerField`): Cantidad de ejemplares involucrados (puede ser positivo o negativo para ajustes).
* **fecha_movimiento** (`DateTimeField`, `auto_now_add=True`): Fecha y hora del movimiento.
* **usuario** (FK, `ForeignKey` a `Usuarios`): Referencia al usuario que realizó el movimiento.
* **referencia_origen** (`CharField`, `max_length=100`, `blank=True`, `null=True`): ID de la venta o del pedido de proveedor relacionado.
* **observaciones** (`TextField`, `blank=True`, `null=True`): Notas adicionales.

## 2. Relaciones entre Entidades

* **Usuarios** (1) --- (M) **Movimientos_Inventario**: Un usuario puede realizar muchos movimientos de inventario.
* **Roles** (1) --- (M) **Usuarios**: Un rol puede ser asignado a muchos usuarios.
* **Proveedores** (1) --- (M) **Pedidos_Proveedores**: Un proveedor puede recibir muchos pedidos.
* **Pedidos_Proveedores** (1) --- (M) **Detalle_Pedido_Proveedor**: Un pedido puede contener muchos ítems de detalle.
* **Libros** (1) --- (M) **Detalle_Pedido_Proveedor**: Un libro puede aparecer en muchos detalles de pedido.
* **Libros** (1) --- (M) **Movimientos_Inventario**: Un libro puede tener muchos movimientos de inventario.