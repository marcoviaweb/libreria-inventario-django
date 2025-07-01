from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Rol
from .forms import RolForm

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

# Create your views here.
