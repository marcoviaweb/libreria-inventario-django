from usuarios.models import Rol, Usuario

rol, created = Rol.objects.get_or_create(nombre_rol='Administrador', defaults={'descripcion': 'Acceso total'})
Usuario.objects.create_superuser(
    username='admin',
    password='admin1234',
    email='admin@admin.com',
    nombre_completo='Administrador',
    rol=rol,
    is_active=True
)
print('Superusuario creado con usuario: admin y contraseña: admin1234')
