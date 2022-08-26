from django.shortcuts import render, get_object_or_404
from .models import *
from administrador.models import Espacos

#======================Home======================

def home(request):
    """PAGINA INICIAL"""
    espaco = Espacos.objects.order_by('nome').all()
    return render(request, 'home.html', {'espacos' : espaco})

def descricao(request, espaco_id):
    """PAGINA DE DESCRIÇÂO DOS ESPAÇO"""
    espaco = get_object_or_404(Espacos, pk=espaco_id)
    return render(request, 'descricao.html', {'espaco' : espaco})

#======================Reserva====================

def registro(request):
    """PAGINA DE RESERVA DE ESPAÇO"""
    return render(request, 'registro.html')
