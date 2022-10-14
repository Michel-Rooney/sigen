from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from administrador.models import Espacos
from django.contrib import messages
from .models import Registro
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .utils import *

#======================Home======================

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
        
        html_content = render_to_string('emails/contate_me.html', {
            'nome' : nome, 'email' : email, 'subject' : subject, 'mensagem' : mensagem
        })
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives('Contate-me', text_content, settings.EMAIL_HOST_USER, ['contatestedeteste30@gmail.com'])
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return redirect('/')


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

        
        if not agente_is_valid(request, agente):
            print('01')
            return redirect('registro')
        if not email_is_valid(request, email):
            print('02')
            return redirect('registro')
        if not empresa_is_valid(request, empresa):
            print('03')
            return redirect('registro')
        if not nome_evento_is_valid(request, nome_evento):
            print('04')
            return redirect('registro')
        if not descricao_is_valid(request, descricao):
            print('05')
            return redirect('registro')
        if not hora_registro_is_valid(request, data_reserva, hora_inicio):
            print('06')
            return redirect('registro')

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
            data_reserva=data_reserva,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim)
        registro.save()

        messages.success(request, 'Registro de evento realizado com sucesso')
        return redirect('registro')

    else:
        return render(request, 'registro.html')
