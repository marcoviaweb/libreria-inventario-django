from django.urls import path
from .views import LibroCreateView, LibroListView

urlpatterns = [
    path('', LibroListView.as_view(), name='libro_list'),
    path('nuevo/', LibroCreateView.as_view(), name='libro_create'),
]