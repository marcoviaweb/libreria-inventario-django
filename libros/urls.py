from django.urls import path
from .views import LibroCreateView, LibroListView, LibroUpdateView

urlpatterns = [
    path('', LibroListView.as_view(), name='libro_list'),
    path('nuevo/', LibroCreateView.as_view(), name='libro_create'),
    path('<int:pk>/editar/', LibroUpdateView.as_view(), name='libro_update'),
]