from django.contrib import messages
from .models import Registro


def agente_is_valid(request, agente):
    if not agente.strip():
        messages.error(request, 'Erro de preenchimento no campo agente')
        return False
    return True

def email_is_valid(request, email):
    if not email.strip():
        messages.error(request, 'Erro de preenchimento no campo Email')
        return False
    return True

def empresa_is_valid(request, empresa):
    if not empresa.strip():
        messages.error(request, 'Erro de preenchimento no campo nome da empresa')
        return False
    return True

def nome_evento_is_valid(request, nome_evento):
    if not nome_evento.strip():
        messages.error(request, 'Erro de preenchimento no cammpo nome do evento')
        return False
    return True

def descricao_is_valid(request, descricao):
    if not descricao.strip():
        messages.error(request, 'Erro de preenchimento no campo descrição')
        return False
    return True

def hora_registro_is_valid(request, data_reserva, hora_inicio):
    registro = Registro.objects.filter(data_reserva=data_reserva, hora_inicio=hora_inicio).first()
    if registro:
        messages.error(request, 'O horario na data escolhida já está ocupado')
        return False
    return True
