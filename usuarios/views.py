from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Rol, Usuario
from .forms import RolForm, UsuarioCreationForm, UsuarioChangeForm

class RolListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Rol
    template_name = 'usuarios/rol_list.html'
    context_object_name = 'roles'
    permission_required = 'usuarios.view_rol'
    
class RolCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'usuarios/rol_form.html'
    success_url = reverse_lazy('rol_list')
    permission_required = 'usuarios.add_rol'

    def form_valid(self, form):
        messages.success(self.request, 'Rol creado exitosamente.')
        return super().form_valid(form)

class RolUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Rol
    form_class = RolForm
    template_name = 'usuarios/rol_form.html'
    success_url = reverse_lazy('rol_list')
    permission_required = 'usuarios.change_rol'

    def form_valid(self, form):
        messages.success(self.request, 'Rol actualizado exitosamente.')
        return super().form_valid(form)

class RolDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Rol
    template_name = 'usuarios/rol_confirm_delete.html'
    success_url = reverse_lazy('rol_list')
    permission_required = 'usuarios.delete_rol'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.can_delete():
            messages.error(request, 'No se puede eliminar el rol porque tiene usuarios asignados.')
            return redirect('rol_list')
        messages.success(request, 'Rol eliminado exitosamente.')
        return super().post(request, *args, **kwargs)

class UsuarioListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'
    permission_required = 'usuarios.view_usuario'

class UsuarioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')
    permission_required = 'usuarios.add_usuario'

    def form_valid(self, form):
        messages.success(self.request, 'Usuario creado exitosamente.')
        return super().form_valid(form)

class UsuarioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioChangeForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')
    permission_required = 'usuarios.change_usuario'

    def form_valid(self, form):
        messages.success(self.request, 'Usuario actualizado exitosamente.')
        return super().form_valid(form)

class UsuarioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')
    permission_required = 'usuarios.delete_usuario'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        messages.success(request, 'Usuario deshabilitado exitosamente.')
        return redirect(self.success_url)

# Create your views here.
