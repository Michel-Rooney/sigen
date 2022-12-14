from django.urls import path
from . import views

urlpatterns =[
    #Login
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name = 'logout'),
    #Pagina de Adm
    path('administrador/', views.administrador, name='administrador'),
    #Listar Usuários
    path('gerenciar_usuario/', views.gerenciar_usuario, name= 'gerenciar_usuario'),
    #Listar Reservas
    path('gerenciar_reserva/', views.gerenciar_reserva, name='gerenciar_reserva'),
    #check-in/out
    path('check_in/', views.check_in, name='check_in'),
    path('realizar_check_in/<int:id>', views.realizar_check_in, name='realizar_check_in'),
    path('check_out/', views.check_out, name='check_out'),
    path('realizar_check_out/<int:id>', views.realizar_check_out, name='realizar_check_out'),
    #Relátorios
    path('gerenciar_relatorios', views.gerenciar_relatorios, name='gerenciar_relatorios'),
    path('relatorio', views.relatorio, name='relatorio'),
    #Registrar novo Adm
    path('adicionar_adm/', views.adicionar_adm, name = 'adicionar_adm'),
    path('editar_adm/<int:usuario_id>', views.editar_adm, name = 'editar_adm'),
    path('deletar_adm/<int:usuario_id>', views.deletar_adm, name='deletar_adm'),
    path('buscar_adm/', views.buscar_adm, name= 'buscar_adm'),
    #Gerenciamento de Espaços
    path('gerenciar_espacos/', views.gerenciar_espacos, name='gerenciar_espacos'),
    path('adicionar_espaco/', views.adicionar_espaco, name='adicionar_espaco'),
    path('remover_espaco/', views.remover_espaco, name='remover_espaco'),
    path('remover_espaco/<int:espaco_id>', views.remover_espaco_id, name='remover_espaco_id'),
    path('editar_espaco/', views.editar_espaco, name='editar_espaco'),
    path('editar_espaco/<int:espaco_id>', views.editar_espaco_id, name='editar_espaco_id'),
    #Abertura de Chamado
    path('abrir_chamado/',views.abrir_chamado,name='abrir_chamado'),
    path('cancelar_reserva/<int:id>', views.cancelar_reserva, name='cancelar_reserva'),
]