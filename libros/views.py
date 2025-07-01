from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .models import Libro
from .forms import LibroForm

class LibroCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/libro_form.html'
    success_url = reverse_lazy('libro_create')
    permission_required = 'libros.add_libro'

    def form_valid(self, form):
        messages.success(self.request, 'Libro registrado exitosamente.')
        return super().form_valid(form)

class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'libros/libro_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        titulo = self.request.GET.get('titulo', '').strip()
        autor = self.request.GET.get('autor', '').strip()
        isbn = self.request.GET.get('isbn', '').strip()
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        if autor:
            queryset = queryset.filter(autor__icontains=autor)
        if isbn:
            queryset = queryset.filter(isbn__icontains=isbn)
        return queryset.order_by('titulo')

# Create your views here.
