from django.urls import path
from .views import RolListView, RolCreateView, RolUpdateView, RolDeleteView

urlpatterns = [
    path('roles/', RolListView.as_view(), name='rol_list'),
    path('roles/nuevo/', RolCreateView.as_view(), name='rol_create'),
    path('roles/<int:pk>/editar/', RolUpdateView.as_view(), name='rol_update'),
    path('roles/<int:pk>/eliminar/', RolDeleteView.as_view(), name='rol_delete'),
]