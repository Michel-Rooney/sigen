from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.reserva.urls')),
    path('adm/', include('apps.administrador.urls')),
    path('admin/', admin.site.urls),
]
