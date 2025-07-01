from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.deprecation import MiddlewareMixin

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Permitir acceso a login, logout, admin y archivos estáticos
        allowed = [
            '/login/', '/logout/', '/admin/', '/accounts/profile/'
        ]
        if request.path.startswith(settings.STATIC_URL):
            return None
        if request.user.is_authenticated or any(request.path.startswith(a) for a in allowed):
            return None
        from django.shortcuts import redirect
        return redirect('login')

# En settings.py, agregar 'libreria_inventario.middleware.LoginRequiredMiddleware' al MIDDLEWARE después de AuthenticationMiddleware.
