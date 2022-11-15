from django.contrib import admin
from .models import *

admin.site.register(Registro)
# admin.site.register(DiasDisponiveis)
# admin.site.register(HorariosDisponiveis)
admin.site.register(Confirmacao)
admin.site.register(ReservasFinalizadas)
admin.site.register(ReservasCanceladas)
