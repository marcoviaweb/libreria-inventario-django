from django.urls import path
from .views import EntradaManualView

urlpatterns = [
    path('entrada-manual/', EntradaManualView.as_view(), name='entrada_manual'),
]
