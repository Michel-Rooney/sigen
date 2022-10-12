from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from administrador.models import Espacos
from django.contrib import messages

#from reserva.models import Registro
from .models import Registro
#======================Home======================

def home(request):
    """PAGINA INICIAL"""
    espaco = Espacos.objects.order_by('nome').all()
    return render(request, 'index.html', {'espacos' : espaco})

def descricao(request, espaco_id):
    """PAGINA DE DESCRIÇÂO DOS ESPAÇO"""
    espaco = get_object_or_404(Espacos, pk=espaco_id)
    return render(request, 'descricao.html', {'espaco' : espaco})

#======================Reserva====================

def registro(request):
    """PAGINA DE RESERVA DE ESPAÇO"""


    if request.method == 'POST':

    # Dados do Agente
        agente = request.POST['nome-agente']
        mantenedor = request.POST['tipo-empresa'] #  tenho que solucionar o probelma da seleção
        cpf = request.POST['numero-cpf']
        email = request.POST['email']
        telefone = request.POST['telefone']
    # Dados da Empresa
        empresa = request.POST['nome-empresa']
        cnpj = request.POST['numero-cnpj']
    #Dados do Evento
        nome_evento = request.POST['nome-evento'] # não existe esse atributo no banco de dados
        descricao = request.POST['descricao-evento']
        #lista_participantes = request.POST['lista-participante'] # Como armazenar isso no banco de dados
        if not agente.strip():
            messages.error(request, 'Erro de preenchimento no campo agente')
            print("Erro no campo agente")
            return redirect('registro')
        if not email.strip():
            messages.error(request, 'Erro de preenchimento no campo Email')
            print("Erro no campo email")
            return redirect('registro')
        if not empresa.strip():
            messages.error(request, 'Erro de preenchimento no campo nome da empresa')
            print("O campo deve ser preenchido corretamente!")
            return redirect('registro')
        if not nome_evento.strip():
            messages.error(request, 'Erro de preenchimento no cammpo nome do evento')
            print("O campo deve ser preenchido corretamente!")
            return redirect('registro')
        if not descricao.strip():
            messages.error(request, 'Erro de preenchimento no campo descrição')
            print("O campo deve ser preenchido corretamente!")
            return redirect('registro')

        registro = Registro.objects.create(agente=agente,
                                           mantenedor=mantenedor,
                                           cpf=cpf,
                                           email=email,
                                           telefone=telefone,
                                           empresa=empresa,
                                           cnpj=cnpj,
                                           nome_evento=nome_evento,
                                           descricao=descricao)
                                           #lista_partiipantes=lista_participantes)
        registro.save()

        messages.success(request, 'Registro de evento realizado com sucesso')
        return redirect('registro')

    else:
        return render(request, 'reserva.html')
