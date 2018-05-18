""" Define padrões de URL para users."""

from django.urls import path

# Importamos a view de login default
from django.contrib.auth.views import login
from . import views

app_name = 'users'

urlpatterns = [
    # Quando Django lê esse URL, a palavra users diz a ele para consultar
    # users/urls.py, e login lhe diz para enviar requisições à view login
    # default de Django(observe que o argumento da view é login, e não
    # views.login).Como não estamos escrevendo nossa própria função de view,
    # passamos um dicionário que diz ao Django em que lugar ele poderá encontrar
    # o template de login. Esse template fará parte da aplicação users, e não de
    # learning_logs.
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
]
