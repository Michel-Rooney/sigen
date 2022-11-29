from ..administrador.validar.validate import valida_email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.conf import settings
from .models import Confirmacao
from .models import Registro
from hashlib import sha256
import random



# ==================== RESERVA ====================
def registro_is_valid(request, agente: str, email: str, empresa: str, nome_evento: str, descricao: str, data_reserva: str, hora_inicio: str) -> bool:
    registro = Registro.objects.filter(data_reserva=data_reserva, hora_inicio=hora_inicio).first()
    if not agente.strip():
        messages.error(request, 'Erro de preenchimento no campo agente')
        return False
    if not email.strip():
        messages.error(request, 'Erro de preenchimento no campo Email')
        return False
    if not valida_email(email):
        messages.error(request, 'Esse email não é válido')
        return False
    if not empresa.strip():
        messages.error(request, 'Erro de preenchimento no campo nome da empresa')
        return False
    if not nome_evento.strip():
        messages.error(request, 'Erro de preenchimento no cammpo nome do evento')
        return False
    if not descricao.strip():
        messages.error(request, 'Erro de preenchimento no campo descrição')
        return False
    if registro:
        messages.error(request, 'O horario na data escolhida já está ocupado')
        return False
    return True

# ==================== EMAIL ====================
def email_html(path_template: str, assunto: str, para: list, conteudo) -> dict:
    
    html_content = render_to_string(path_template, conteudo)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, para)

    email.attach_alternative(html_content, "text/html")
    email.send()
    return {'status': 1}

def make_token(agente: str, email: str, registro: str) -> str:
    key = random.randint(100,2000)
    token = sha256(f'{agente}{key}{email}'.encode()).hexdigest()
    ativacao = Confirmacao(token=token, registro=registro)
    ativacao.save()
    return f'127.0.0.1:8000/ativar_conta/{token}'