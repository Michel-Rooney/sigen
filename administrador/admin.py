from django.contrib import admin
from .models import *

class Espaco(admin.ModelAdmin):
    list_display= ('id','nome')
    list_display_links = ('id','nome')
    
admin.site.register(Espacos,Espaco)
admin.site.register(NivelUsuario)
