# Especificaciones del Sistema de Inventario para Librería

## 1. Visión General del Proyecto

Se requiere desarrollar un **Sistema de Gestión de Inventario para una Librería**, con un enfoque en la **simplicidad, eficiencia y facilidad de uso**. El sistema debe permitir el control de los libros, su stock, la gestión de pedidos a proveedores, el registro de ventas básicas y el control de acceso de usuarios.

## 2. Tecnologías a Utilizar

* **Backend Framework:** Django (Python)
* **Frontend Framework/CSS:** Bootstrap (para un diseño responsivo y consistente)
* **Base de Datos:** SQLite (para desarrollo inicial, extensible a PostgreSQL/MySQL en producción si es necesario, pero la configuración inicial debe ser con SQLite para simplicidad).

## 3. Módulos / Funcionalidades Requeridas

El sistema estará compuesto por los siguientes módulos principales:

### 3.1. Gestión de Libros (Catálogo)
* **Funcionalidad:** Registrar, visualizar, buscar, filtrar y editar la información detallada de cada libro.
* **Atributos Clave por Libro:** Título, Autor(es), ISBN (único), Editorial, Precio de Venta, Costo de Adquisición, Categoría/Género, Descripción Corta/Sinopsis.

### 3.2. Gestión de Stock (Inventario Físico)
* **Funcionalidad:** Controlar las cantidades disponibles de cada libro.
* **Operaciones:**
    * **Ver Cantidad Disponible:** Mostrar el stock actual.
    * **Entrada de Stock:** Registrar la adición de libros al inventario (aumenta el stock).
    * **Salida de Stock (Ventas):** Registrar la venta de libros (disminuye el stock).
    * **Ajustes de Inventario:** Modificar manualmente el stock por discrepancias (pérdidas, daños, correcciones).
    * **Alertas de Stock Bajo:** Notificación cuando el stock de un libro cae por debajo de un umbral predefinido.

### 3.3. Gestión de Pedidos a Proveedores
* **Funcionalidad:** Simplificar el proceso de reabastecimiento y llevar un control de los proveedores y los pedidos realizados.
* **Sub-módulos:**
    * **Registro de Proveedores:** Almacenar datos de contacto de proveedores (Nombre, Contacto, Teléfono, Email).
    * **Creación de Pedidos:** Generar nuevas órdenes de compra, seleccionando libros y cantidades. Debe permitir asociar el pedido a un proveedor.
    * **Recepción de Pedidos:** Marcar los artículos recibidos, actualizando automáticamente el stock. Debe permitir recepciones parciales.

### 3.4. Gestión de Ventas
* **Funcionalidad:** Registrar la venta de uno o varios libros, actualizando el stock de forma automática.
* **Operaciones:**
    * **Registrar Venta:** Seleccionar libros del catálogo, especificar cantidades y generar un registro de venta. Esto debe desencadenar la disminución del `stock_actual` en el módulo de inventario.

### 3.5. Gestión de Usuarios y Roles
* **Funcionalidad:** Controlar el acceso al sistema y las acciones permitidas según el tipo de usuario.
* **Roles Definidos:**
    * **Administrador:** Acceso completo a todas las funcionalidades (gestión de libros, stock, pedidos, ventas, usuarios, reportes).
    * **Encargado de Inventario:** Acceso a gestión de libros, stock (entradas, ajustes), pedidos a proveedores y reportes relacionados. No gestiona usuarios.
    * **Vendedor/Cajero:** Acceso para registrar ventas, buscar libros y consultar el stock disponible. No puede modificar el inventario directamente ni gestionar pedidos o usuarios.

### 3.6. Reportes Básicos
* **Funcionalidad:** Generar informes simples para la toma de decisiones.
* **Reportes Clave:**
    * **Libros en Stock:** Listado de todos los libros con sus cantidades actuales.
    * **Libros con Stock Bajo:** Informe de libros que necesitan reabastecimiento.
    * **Movimientos de Inventario:** Historial de entradas/salidas de stock.
    * **Historial de Pedidos a Proveedores:** Listado de pedidos realizados y su estado.
    * **Reportes de Ventas:** Resumen de ventas (ej. por día, por libro).

## 4. Estructura de Acceso por Rol (Tabla de Permisos)

| Módulo / Funcionalidad Principal | Administrador | Encargado de Inventario | Vendedor/Cajero |
| :------------------------------- | :-----------: | :---------------------: | :-------------: |
| **1. Gestión de Libros (Catálogo)** |               |                         |                 |
| Registro de Libros               |      Sí       |           Sí            |       No        |
| Edición de Información de Libros |      Sí       |           Sí            |       No        |
| Búsqueda y Filtrado de Libros    |      Sí       |           Sí            |       Sí        |
| **2. Gestión de Stock** |               |                         |                 |
| Ver Cantidad Disponible          |      Sí       |           Sí            |       Sí        |
| Registrar Entrada de Stock       |      Sí       |           Sí            |       No        |
| Realizar Ajustes de Inventario   |      Sí       |           Sí            |       No        |
| **3. Gestión de Pedidos a Proveedores** |               |                         |                 |
| Registro de Proveedores          |      Sí       |           Sí            |       No        |
| Creación de Pedidos              |      Sí       |           Sí            |       No        |
| Recepción de Pedidos             |      Sí       |           Sí            |       No        |
| **4. Gestión de Ventas** |               |                         |                 |
| Registrar Venta                  |      Sí       |           Sí            |       Sí        |
| **5. Gestión de Usuarios y Roles** |               |                         |                 |
| Registro de Usuarios             |      Sí       |           No            |       No        |
| Definición y Asignación de Roles |      Sí       |           No            |       No        |
| **6. Reportes Básicos** |               |                         |                 |
| Libros en Stock                  |      Sí       |           Sí            |       Sí        |
| Libros con Stock Bajo            |      Sí       |           Sí            |       No        |
| Movimientos de Inventario        |      Sí       |           Sí            |       No        |
| Historial de Pedidos             |      Sí       |           Sí            |       No        |
| Reportes de Ventas               |      Sí       |           Sí            |       Sí        |

## 5. Buenas Prácticas de Desarrollo Requeridas

El agente debe adherirse a las siguientes buenas prácticas:

### 5.1. Arquitectura de Proyecto Django
* **Modularidad:** Usar aplicaciones Django separadas para cada módulo principal (ej. `libros`, `inventario`, `pedidos`, `ventas`, `usuarios`, `reportes`).
* **Separación de Intereses (MVT):** Asegurar que Modelos, Vistas y Templates tengan responsabilidades únicas y bien definidas.
* **Configuración:** Manejar `settings.py` de forma organizada; considerar variables de entorno para datos sensibles.

### 5.2. Diseño de Base de Datos (Modelos Django)
* **Claridad y Coherencia:** Nombres de campos claros y consistentes.
* **Relaciones:** Correcta definición de `ForeignKey`, `OneToOneField`, `ManyToManyField`.
* **Tipos de Datos:** Uso de tipos de campo de Django apropiados (`CharField`, `IntegerField`, `DecimalField`, `DateField`, `BooleanField`, `TEXT`).
* **Validación:** Implementar validaciones a nivel de modelo (ej. `unique=True` para ISBN).
* **`__str__` Métodos:** Definir para todos los modelos para una mejor representación.

### 5.3. Vistas y Lógica de Negocio
* **Vistas Basadas en Clases (CBV):** Preferirlas sobre funciones cuando sea posible.
* **Lógica en Modelos:** La lógica de negocio compleja debe residir en los modelos o en funciones auxiliares (`managers`, `utils.py`), manteniendo las vistas delgadas.
* **Formularios Django:** Utilizar `forms.Form` o `forms.ModelForm` para la entrada y validación de datos.
* **Redirecciones y Mensajes:** Usar `redirect` y el `messages framework` para feedback al usuario.
* **Transacciones (si aplica):** Considerar transacciones atómicas para operaciones críticas de base de datos.

### 5.4. Diseño Frontend (Bootstrap y Templates)
* **Template Base:** Crear un `base.html` con la estructura común.
* **Bootstrap Responsivo:** Integrar Bootstrap para un diseño adaptable a diferentes dispositivos.
* **DRY (Don't Repeat Yourself):** Reutilizar fragmentos de HTML con `{% include %}`.
* **Formularios con Bootstrap:** Renderizar formularios de Django con estilos de Bootstrap (considerar `django-crispy-forms` si es útil).
* **JavaScript:** Mínimo y solo cuando sea estrictamente necesario.

### 5.5. Seguridad
* **Autenticación y Autorización:** Usar el sistema de autenticación de Django. Implementar `@login_required` y `PermissionRequiredMixin` para control de acceso por rol/permiso.
* **Protección CSRF:** Asegurar la inclusión de `{% csrf_token %}` en formularios.
* **Sanitización:** No confiar en la entrada directa del usuario.
* **Contraseñas Seguras:** Aprovechar el hashing de contraseñas de Django.

### 5.6. Mantenimiento y Escalabilidad
* **Control de Versiones:** Usar Git con commits descriptivos.
* **Entornos Virtuales:** Trabajar siempre en `venv`.
* **Pruebas (Opcional pero recomendado):** Si el agente tiene capacidad, considerar la inclusión de pruebas unitarias/integración básicas.
* **Documentación:** Comentar el código.

## 6. Historias de Usuario y Criterios de Aceptación

Para un desarrollo incremental, cada funcionalidad se descompondrá en Historias de Usuario (HU) con sus respectivos Criterios de Aceptación (CA). Esto guiará la implementación paso a paso. Las historias están priorizadas para un flujo de desarrollo lógico.

### 6.1. Prioridad 1: Módulo de Usuarios y Roles (Core del sistema)

#### HU 6.1.1: Gestión de Roles
* **Como** administrador,
* **Quiero** poder definir diferentes roles (ej. Administrador, Encargado de Inventario, Vendedor/Cajero)
* **Para** asignar distintos niveles de acceso y permisos en el sistema.
* **Criterios de Aceptación:**
    * CA 6.1.1.1: El sistema debe permitir crear nuevos roles con un nombre y una descripción.
    * CA 6.1.1.2: El sistema debe permitir ver una lista de todos los roles existentes.
    * CA 6.1.1.3: El sistema debe permitir editar el nombre y la descripción de un rol existente.
    * CA 6.1.1.4: El sistema debe prevenir la eliminación de un rol si hay usuarios asignados a él.

#### HU 6.1.2: Gestión de Usuarios
* **Como** administrador,
* **Quiero** poder crear, editar y eliminar usuarios del sistema
* **Para** controlar quién tiene acceso y qué rol desempeña cada empleado.
* **Criterios de Aceptación:**
    * CA 6.1.2.1: El sistema debe permitir crear un nuevo usuario con nombre de usuario, contraseña, nombre completo, email y asignarle un rol existente.
    * CA 6.1.2.2: El sistema debe permitir ver una lista de todos los usuarios registrados, mostrando su rol.
    * CA 6.1.2.3: El sistema debe permitir editar la información de un usuario existente, incluyendo su rol.
    * CA 6.1.2.4: El sistema debe permitir deshabilitar o eliminar un usuario.
    * CA 6.1.2.5: Un usuario debe poder iniciar sesión con sus credenciales y su acceso debe ser restringido según su rol.

### 6.2. Prioridad 2: Módulo de Libros (Catálogo Básico)

#### HU 6.2.1: Registro de Nuevos Libros
* **Como** encargado de inventario,
* **Quiero** poder añadir nuevos títulos al catálogo de la librería
* **Para** tener un registro completo de los libros disponibles.
* **Criterios de Aceptación:**
    * CA 6.2.1.1: El sistema debe tener un formulario con campos para Título, Autor, ISBN, Editorial, Precio de Venta, Costo de Adquisición, Categoría, Sinopsis.
    * CA 6.2.1.2: El ISBN debe ser un campo único y obligatorio.
    * CA 6.2.1.3: Al guardar un nuevo libro, el `stock_actual` debe inicializarse en 0 y `stock_minimo` en un valor por defecto (ej. 5).
    * CA 6.2.1.4: El sistema debe mostrar un mensaje de éxito al guardar el libro.

#### HU 6.2.2: Visualización y Búsqueda de Libros
* **Como** vendedor o encargado de inventario,
* **Quiero** poder ver un listado de todos los libros y buscar títulos específicos
* **Para** consultar rápidamente la información y el stock.
* **Criterios de Aceptación:**
    * CA 6.2.2.1: El sistema debe mostrar una tabla con los libros, mostrando Título, Autor, ISBN, Precio de Venta y Stock Actual.
    * CA 6.2.2.2: Debe existir un campo de búsqueda por Título, Autor o ISBN que filtre la tabla de resultados.
    * CA 6.2.2.3: La tabla debe ser paginable si hay muchos libros.

#### HU 6.2.3: Edición de Información de Libros
* **Como** encargado de inventario,
* **Quiero** poder modificar los detalles de un libro existente
* **Para** corregir errores o actualizar la información.
* **Criterios de Aceptación:**
    * CA 6.2.3.1: Cada libro en la lista debe tener una opción para "Editar".
    * CA 6.2.3.2: El formulario de edición debe precargar la información existente del libro.
    * CA 6.2.3.3: Al guardar los cambios, la información del libro debe actualizarse en el catálogo.

### 6.3. Prioridad 3: Gestión Básica de Stock (Movimientos Manuales)

#### HU 6.3.1: Registro de Entrada de Stock (Manual)
* **Como** encargado de inventario,
* **Quiero** poder registrar la entrada manual de ejemplares de un libro
* **Para** actualizar el stock cuando llegan nuevas unidades (sin ser por pedido).
* **Criterios de Aceptación:**
    * CA 6.3.1.1: El sistema debe permitir seleccionar un libro y especificar la cantidad de unidades que ingresan.
    * CA 6.3.1.2: Al registrar la entrada, el `stock_actual` del libro debe aumentar en la cantidad especificada.
    * CA 6.3.1.3: Se debe registrar un movimiento de inventario con tipo "Entrada Manual" o similar.

#### HU 6.3.2: Registro de Ajustes de Stock
* **Como** encargado de inventario,
* **Quiero** poder realizar ajustes manuales al stock de un libro (aumentar o disminuir)
* **Para** corregir discrepancias o registrar pérdidas/daños.
* **Criterios de Aceptación:**
    * CA 6.3.2.1: El sistema debe permitir seleccionar un libro y especificar una cantidad para ajustar (positiva o negativa).
    * CA 6.3.2.2: Se debe requerir una razón o comentario para el ajuste.
    * CA 6.3.2.3: El `stock_actual` del libro debe modificarse según el ajuste.
    * CA 6.3.2.4: Se debe registrar un movimiento de inventario con tipo "Ajuste Positivo" o "Ajuste Negativo".

### 6.4. Prioridad 4: Gestión de Ventas

#### HU 6.4.1: Registrar Venta de un Libro
* **Como** vendedor o cajero,
* **Quiero** poder registrar la venta de uno o varios libros
* **Para** disminuir el stock automáticamente y llevar un control de las transacciones.
* **Criterios de Aceptación:**
    * CA 6.4.1.1: El sistema debe permitir seleccionar uno o varios libros del catálogo para la venta.
    * CA 6.4.1.2: Se debe especificar la cantidad de cada libro vendido.
    * CA 6.4.1.3: Al confirmar la venta, el `stock_actual` de cada libro vendido debe disminuir en la cantidad correspondiente.
    * CA 6.4.1.4: Se debe registrar un movimiento de inventario con tipo "Salida por Venta" para cada libro vendido.
    * CA 6.4.1.5: El sistema debe mostrar el total de la venta.

### 6.5. Prioridad 5: Gestión de Proveedores y Pedidos

#### HU 6.5.1: Registro y Gestión de Proveedores
* **Como** encargado de inventario,
* **Quiero** poder registrar y gestionar los datos de mis proveedores
* **Para** tener un listado actualizado de contactos.
* **Criterios de Aceptación:**
    * CA 6.5.1.1: El sistema debe permitir crear, ver, editar y eliminar proveedores (Nombre, Contacto, Teléfono, Email).
    * CA 6.5.1.2: El nombre del proveedor debe ser único.

#### HU 6.5.2: Creación de Pedidos a Proveedores
* **Como** encargado de inventario,
* **Quiero** poder crear un nuevo pedido a un proveedor
* **Para** ordenar la reposición de libros.
* **Criterios de Aceptación:**
    * CA 6.5.2.1: El sistema debe permitir seleccionar un proveedor y añadir múltiples libros al pedido con sus cantidades solicitadas.
    * CA 6.5.2.2: El estado inicial del pedido debe ser "Pendiente".

#### HU 6.5.3: Recepción de Pedidos
* **Como** encargado de inventario,
* **Quiero** poder registrar la recepción de un pedido de proveedor
* **Para** actualizar el stock y el estado del pedido.
* **Criterios de Aceptación:**
    * CA 6.5.3.1: El sistema debe permitir seleccionar un pedido pendiente.
    * CA 6.5.3.2: Se debe poder especificar cuántas unidades de cada libro se recibieron (permitiendo recepción parcial).
    * CA 6.5.3.3: La cantidad de `stock_actual` de los libros recibidos debe aumentar.
    * CA 6.5.3.4: El estado del pedido debe actualizarse a "Completado" o "Recibido Parcial" según corresponda.
    * CA 6.5.3.5: Se deben registrar movimientos de inventario con tipo "Entrada por Compra".

### 6.6. Prioridad 6: Reportes

#### HU 6.6.1: Reporte de Libros en Stock
* **Como** cualquier usuario,
* **Quiero** poder ver un reporte del inventario actual
* **Para** conocer la disponibilidad de libros.
* **Criterios de Aceptación:**
    * CA 6.6.1.1: El reporte debe mostrar el Título, ISBN y Stock Actual de todos los libros.
    * CA 6.6.1.2: Debe ser accesible desde el menú principal.

#### HU 6.6.2: Reporte de Libros con Stock Bajo
* **Como** encargado de inventario,
* **Quiero** poder ver rápidamente qué libros necesitan reponerse
* **Para** planificar futuros pedidos.
* **Criterios de Aceptación:**
    * CA 6.6.2.1: El reporte debe listar los libros cuyo `stock_actual` sea menor o igual al `stock_minimo`.
    * CA 6.6.2.2: Debe mostrar Título, ISBN, Stock Actual y Stock Mínimo.

#### HU 6.6.3: Reporte de Movimientos de Inventario
* **Como** encargado de inventario,
* **Quiero** poder consultar un historial de entradas y salidas de libros
* **Para** auditar y entender el flujo del inventario.
* **Criterios de Aceptación:**
    * CA 6.6.3.1: El reporte debe mostrar la Fecha, Tipo de Movimiento, Libro afectado, Cantidad y el Usuario que lo realizó.
    * CA 6.6.3.2: Debe permitir filtrar por tipo de movimiento o por rango de fechas.

#### HU 6.6.4: Reporte de Ventas
* **Como** administrador o encargado de inventario,
* **Quiero** ver un resumen de las ventas realizadas
* **Para** analizar el rendimiento y la demanda.
* **Criterios de Aceptación:**
    * CA 6.6.4.1: El reporte debe mostrar las ventas con la fecha, los libros vendidos y el total de la transacción.
    * CA 6.6.4.2: Debe permitir filtrar por rango de fechas o por libro.