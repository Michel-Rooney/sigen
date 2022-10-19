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
    #Registrar novo Adm
    path('registro_adm/', views.registro_adm, name = 'registro_adm'),
    #Gerenciamento de Espaços
    path('gerenciar_espaco/', views.gerenciar_espaco, name='gerenciar_espaco'),
    path('adicionar_espaco/', views.adicionar_espaco, name='adicionar_espaco'),
    path('remover_espaco/', views.remover_espaco, name='remover_espaco'),
    path('remover_espaco/<int:espaco_id>', views.remover_espaco_id, name='remover_espaco_id'),
    path('editar_espaco/', views.editar_espaco, name='editar_espaco'),
    path('editar_espaco/<int:espaco_id>', views.editar_espaco_id, name='editar_espaco_id')
]