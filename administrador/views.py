from re import A
from django.shortcuts import render
from .models import NivelUsuario, Espacos
from reserva.models import Confirmacao, Registro
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime,date,time
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
import os
from django.contrib.auth.decorators import login_required
from core.settings import BASE_DIR

#========================LOGIN ADM=======================

def login(request):
    """PAGINA DE LOGIN DO ADMINISTRADOR"""
    if request.method ==  'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        #SE O EMAIL FOR VALIDO E CONSTAR NO BANCO
        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email = email).values_list('username',flat=True).get()
            user = auth.authenticate(request, username = nome, password = senha)
            if user is not None:
                auth.login(request, user)
                return redirect('administrador')
    return render(request,'login.html')

def logout(request):
    """REALIZAÇÂO DE LOGOUT DO USUARIO"""
    auth.logout(request)
    return redirect('/adm/login')

#========================END LOGIN ADM=======================

#========================ADMINISTRADOR=======================
    
@login_required(login_url='/adm/login')
def administrador(request):
    """PAGINA DE ADMINISTRADOR"""
    usuario = request.user.id
    conteudo = {'nivel': get_object_or_404(NivelUsuario, usuario=usuario)}
    return render(request, 'administrador.html', conteudo)


@login_required(login_url='/adm/login')
def gerenciar_usuario(request):
    """Página de Listagem de Usuários Administradores do Sistema"""
    user = {'user': User.objects.all()}
    return render(request, 'gerenciar_usuario.html', user)

@login_required(login_url='/adm/login')
def gerenciar_reserva(request):
    """Página de Listagem de Reservas Confirmadas"""
    registro = {'registro': Registro.objects.all()}
    return render(request, 'gerenciar_reserva.html', registro)

@login_required(login_url='/adm/login')
def registro_adm(request):
    """PAGINA DE REGISTRO DE NOVO ADMINISTRADOR"""
    if request.method == 'POST':
        nome = request.POST['nome_usuario']
        email = request.POST['email']
        senha = request.POST['senha']

#AREA RESPONSAVEL POR GERENCIAMENTO DE ESPAÇOS

@login_required(login_url='/adm/login')
def gerenciar_espaco(request):
    """PAGINA DE GERENCIAMENTO DE ESPAÇOS"""
    return render(request, 'espacos/gerenciar_espaco.html')

@login_required(login_url='/adm/login')
def remover_espaco(request):
    """PAGINA DE REMOÇÂO DE ESPAÇO"""
    conteudo = {'espacos': Espacos.objects.order_by('nome').all()}
    return render(request, 'espacos/remover_espaco.html', conteudo)

@login_required(login_url='/adm/login')
def remover_espaco_id(request, espaco_id):
    """REMOVER ESPAÇO ESPECIFICO"""
    espaco = get_object_or_404(Espacos, pk=espaco_id)
    os.remove(os.path.join(BASE_DIR, espaco.imagem1.path))
    espaco.delete()
    return redirect('/remover_espaco')

@login_required(login_url='/adm/login')
def editar_espaco(request):
    """PAGINA DE EDIÇÂO DOS ESPAÇOS"""
    espaco = Espacos.objects.all()
    return render(request, 'espacos/editar_espaco.html', {'espacos' : espaco})

@login_required(login_url='/adm/login')
def editar_espaco_id(request, espaco_id):
    """EDITAR ESPAÇO ESPECIFICO"""
    if request.method == 'POST':
        espaco = Espacos.objects.get(id=espaco_id)
        
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        imagem1 = request.FILES['imagem1']
        # imagem2 = request.FILES['imagem2']
        # imagem3 = request.FILES['imagem3']
        # imagem4 = request.FILES['imagem4']

        try:
            os.remove(os.path.join(BASE_DIR, espaco.imagem1.path))
        except:
            pass

        espaco.nome = nome
        espaco.descricao = descricao
        espaco.imagem1 = imagem1
        espaco.save()
        return redirect('/editar_espaco')

    espaco = get_object_or_404(Espacos, pk=espaco_id)
    return render(request, 'espacos/editar_espaco_id.html', {'espaco' : espaco})

@login_required(login_url='/adm/login')
def adicionar_espaco(request):
    """ADCICIONAR ESPAÇO ESPECIFICO"""
    if request.method == 'POST':

        nome = request.POST['nome']
        descricao = request.POST['descricao']
        imagem1 = request.FILES['imagem1']
        # imagem2 = request.FILES['imagem2']
        # imagem3 = request.FILES['imagem3']
        # imagem4 = request.FILES['imagem4']

        try:
            os.remove(os.path.join(BASE_DIR, espaco.imagem1.path))
        except:
            pass
        
        espaco = Espacos.objects.create(nome=nome, descricao=descricao, imagem1=imagem1)
    
    return render(request, 'espacos/adicionar_espaco.html')

# AREA RESPONSAVEL POR CHECK-IN/OUT

@login_required(login_url='/adm/login')
def check_in(request):
    """PAGINA DE CHECK-IN/OUT"""
    conteudo = {"casos": Confirmacao.objects.filter(check_in=False).all(),
    }
    return render(request, 'check_in.html',conteudo)

@login_required(login_url='/adm/login')
def realizar_check_in(request,id):
    """REALIZAR CHECK IN DAS RESERVAS"""
    checando = get_object_or_404(Confirmacao,pk=id)
    if checando.registro.data_reserva == date.today():
        if checando.check_in == False:
            checando.check_in = True
            checando.horario_checkin = datetime.now().strftime('%H:%M:%S')
        checando.save()
        messages.success(request, 'Check-in realizado com sucesso')
    else:
        messages.error(request, 'Check-in não realizado, verifique a data')
    return redirect('check_in')


def check_out(request):
    """PAGINA DE CHECK-IN/OUT"""
    conteudo = {"casos": Confirmacao.objects.filter(check_in= True,check_out= False).all(),
    }
    return render(request, 'check_out.html',conteudo)

def realizar_check_out(request, id):
    """REALIZAR CHECK IN DAS RESERVAS"""
    checando = get_object_or_404(Confirmacao, pk=id)
    if checando.registro.data_reserva == date.today():
        if checando.check_in == True and checando.check_out == False:
            quantidade = request.POST['quantidade']
            checando.qtd_participantes = quantidade
            checando.horario_checkot = datetime.now().strftime('%H:%M:%S')
        checando.save()
    return redirect('check_out')


#========================END ADMINISTRADOR=======================

