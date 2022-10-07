from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from administrador.models import Espacos

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

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




