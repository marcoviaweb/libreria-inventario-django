from django.urls import path
from .views import (
    RolListView, RolCreateView, RolUpdateView, RolDeleteView,
    UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
)

urlpatterns = [
    path('roles/', RolListView.as_view(), name='rol_list'),
    path('roles/nuevo/', RolCreateView.as_view(), name='rol_create'),
    path('roles/<int:pk>/editar/', RolUpdateView.as_view(), name='rol_update'),
    path('roles/<int:pk>/eliminar/', RolDeleteView.as_view(), name='rol_delete'),

    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/nuevo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario_delete'),
]