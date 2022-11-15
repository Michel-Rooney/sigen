from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns =[
    #Home
    path('', views.home, name='home'),
    path('<int:espaco_id>', views.descricao, name='descricao'),
    #Reservas
    path('registro/<int:espaco_id>', views.registro, name='registro'),
    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta"),
    path('erro', views.erro, name='erro'),
    path('sucesso', views.sucesso, name='sucesso'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)