from django.urls import path
from . import views

urlpatterns =[
    #Login
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name = 'logout'),
    #Pagina de Adm
    path('pagina_administrador/', views.administrador, name='administrador'),
    #check-in/out
    path('check/', views.check, name='check'),
    path('check_in/<int:id>', views.check_in, name='check_in'),
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