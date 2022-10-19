from django.contrib import admin
from .models import *

class Espaco(admin.ModelAdmin):
    list_display= ('id','nome')
    list_display_links = ('id','nome')
    
class Chamados(admin.ModelAdmin):
    list_display= ('id', 'solicitante', 'data', 'ambiente', 'status',)
    list_display_links= ('id', 'solicitante',)
    list_editable= ('status',)

admin.site.register(Espacos,Espaco)
admin.site.register(NivelUsuario)
admin.site.register(Chamado, Chamados)