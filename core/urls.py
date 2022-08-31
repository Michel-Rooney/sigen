from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('reserva.urls')),
    path('adm/', include('administrador.urls')),
    path('admin/', admin.site.urls),
]
