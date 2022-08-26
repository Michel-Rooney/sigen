# Projeto NinnaHub

## Passo a passo

1- Clonar o repositório na maquina
```
git clone https://github.com/Michel-Rooney/sigen
```

2- Abrir a pasta projeto-ninnahub com o VSCode e criar a venv pelo terminal
```
# Precisa ter o python instalado na máquina
python -m venv venv
```

3- Ativar a venv e baixar o requirements.txt
```
# Dá permisão de iniciar a venv
# No powershell admin digitar
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    e digitar A para aceitar todos
    
# Ativar a venv
.\venv\Scripts\activate

# Com a venv ativada
pip install -r requirements.txt
```

4- Usando o django
```
# Iniciar o projeto
python manage.py runserver

# No navegardor digite
http://127.0.0.1:8000/

# Para transitar pelos templates 
# Olhar dentro da pasta registro/urls.py, e digtar juntamente com a url o caminhado escolhido

urlpatterns = [
    path('', views.home, name='home'),
    path('check/', views.check, name='check'),
    path('chamado/', views.abertura_chamado, name='abertura_chamado'),
    path('registro/', views.registro, name='registro'),
    path('<int:espaco_id>', views.descricao, name='descricao')


Ex: http://127.0.0.1:8000/ ------------> home
    http://127.0.0.1:8000/check -------> pagina de check_in/out
    http://127.0.0.1:8000/chamado -----> pagina de registro

```

5- Mandar/Pegar alterações do projeto
```
# Curso completo de git
https://www.youtube.com/watch?v=OuOb1_qADBQ

# Configurar o usuario git
    # Só precisa fazer uma unica fez
    git config --global user.name "seu nome"
    git config --global user.email "seu email"

# Pegar alterações (lembre-se de fazer isso antes mesmo de mexer no projeto, ou mandar suas alterações)
    git pull origin main

# Mandar alterações
    # Adicionar alterações feitas
        git add .

    # Comitar suas alterações
        git commit -m "de forma resumida o que você fez"

    # Mandar alterações
        git push origin main

```
