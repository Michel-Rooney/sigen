from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from administrador.models import Espacos

#======================Home======================

def home(request):
    """PAGINA INICIAL"""
    espaco = Espacos.objects.order_by('nome').all()
    num_espacos = Espacos.objects.count()
    perc = str(float(num_espacos * 100 / num_espacos))
    
    print(perc)
    return render(request, 'index.html', {'espacos' : espaco, 'perc': perc})

def descricao(request, espaco_id):
    """PAGINA DE DESCRIÇÂO DOS ESPAÇO"""
    espaco = get_object_or_404(Espacos, pk=espaco_id)
    return render(request, 'descricao.html', {'espaco' : espaco})

#======================Reserva====================

def registro(request):
    """PAGINA DE RESERVA DE ESPAÇO"""
    if request.method == 'GET':
        return render(request, 'registro.html')
    elif request.method == 'POST':
        nome_agente = request.POST['nome-agente']
        tipo_empresa = request.POST['tipo-empresa']
        numero_cpf = request.POST['numero-cpf']
        email = request.POST['email']
        telefone = request.POST['telefone']
        nome_empresa = request.POST['nome-empresa']
        numero_cnpj = request.POST['numero-cnpj']
        nome_evento = request.POST['nome-evento']
        lista_participante = request.FILES['lista-participante']
        descricao_evento = request.POST['descricao-evento']


        # Está feito supercialmente, ainda a campos faltando
        # try:
        #     registro = Registro.objects.create(agente=nome_agente, mantenedor=tipo_empresa, empresa=nome_empresa,email=email, telefone=telefone,
        #                                     cpf=numero_cpf, cnpj=numero_cnpj, descricao=descricao_evento)
        #     registro.save()
        #     return redirect('/')
        # except:
        #     return redirect('/registro')




