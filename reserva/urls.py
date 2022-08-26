from django.urls import path
from . import views

urlpatterns =[
    #Home
    path('', views.home, name='home'),
    path('<int:espaco_id>', views.descricao, name='descricao'),
    #Reservas
    path('registro/', views.registro, name='registro'),
]