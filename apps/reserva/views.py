from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from apps.administrador.models import Espacos
from django.contrib import messages
from .models import Registro, Confirmacao
from .utils import *



# ==================== Home ====================
def home(request):
    """PAGINA INICIAL"""
    if request.method == 'GET':
        espaco = Espacos.objects.order_by('nome').all()
        num_espacos = Espacos.objects.count()
        perc = str(float(num_espacos * 100 / num_espacos))
        return render(request, 'index.html', {'espacos' : espaco, 'perc': perc})
    elif request.method == 'POST':
        nome = request.POST['name-id']
        email = request.POST['email-id']
        subject = request.POST['subject-id']
        mensagem = request.POST['message']
        
        conteudo = {
            'nome' : nome, 'email' : email, 'subject' : subject, 'mensagem' : mensagem
        }
        email_html('emails/contate_me.html', subject, ['suportesigen@gmail.com'], conteudo)
        return redirect('/')


def descricao(request, espaco_id):
    """PAGINA DE DESCRIÇÂO DOS ESPAÇO"""
    espaco = get_object_or_404(Espacos, pk=espaco_id)
    return render(request, 'descricao.html', {'espaco' : espaco})


# ==================== Reserva ====================
def registro(request, espaco_id):
    """PAGINA DE RESERVA DE ESPAÇO"""
    if request.method == 'POST':
        # Dados do Agente
        espaco = get_object_or_404(Espacos, pk=espaco_id)
        agente = request.POST['nome-agente']
        mantenedor = request.POST['tipo-empresa']
        cpf = request.POST['numero-cpf']
        email = request.POST['email']
        telefone = request.POST['telefone']
    
        # Dados da Empresa
        empresa = request.POST['nome-empresa']
        cnpj = request.POST['numero-cnpj']
    
        # Dados do Evento
        nome_evento = request.POST['nome-evento']
        descricao = request.POST['descricao-evento']
        lista_participantes = request.FILES['lista_participantes']

        # Dados dos horários
        data_reserva = request.POST['data_reserva']
        hora_inicio = request.POST['hora_inicio']
        hora_fim = request.POST['hora_fim'] 


        if not registro_is_valid(request, agente, email, empresa, nome_evento, descricao, data_reserva, hora_inicio):
            return redirect('erro')

        registro = Registro.objects.create(
            agente=agente,
            mantenedor=mantenedor,
            cpf=cpf,
            email=email,
            telefone=telefone,
            empresa=empresa,
            cnpj=cnpj,
            nome_evento=nome_evento,
            descricao=descricao,
            lista_participantes=lista_participantes,
            espacos = espaco,
            data_reserva=data_reserva,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim)
        registro.save()
        messages.success(request, 'Registro de evento realizado com sucesso')

        link_ativacao = make_token(agente, email, registro)
        conteudo = {'agente':agente, 'empresa':empresa, 'nome_evento':nome_evento, 'data_reserva':data_reserva, 'hora_inicio':hora_inicio, 'hora_fim':hora_fim, 'link_ativacao':link_ativacao}

        email_html('emails/confirmacao_registro.html', 'Confirmação de Registro', ['suportesigen@gmail.com'], conteudo)
        return redirect('sucesso')
    else:
        return render(request, 'registro.html')


def ativar_conta(request, token):
    token = get_object_or_404(Confirmacao, token=token)
    if token.ativo:
        messages.warning(request, 'Essa token já foi usado')
        return redirect('registro')
    registro = Registro.objects.get(id=token.registro.id)
    registro.confirmacao_email = True
    registro.save()
    token.ativo = True
    token.save()
    messages.success(request, 'Conta ativa com sucesso')
    return redirect('registro')

def erro(request):
    return render(request,'status/erro.html')
def sucesso(request):
    return render(request,'status/sucesso.html')
