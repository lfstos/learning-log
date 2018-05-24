from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# A função de logout_view, recebe esse nome para distingui-la da função
# logout(), que chamaremos a partir da view.
# Essa função logout_view() é simples: simplesmente importamos a função
# logout() de Django, chamamos essa função e redirecionamos o usuário para a
# página inicial.
def logout_view(request):
    """Faz logout do usuário."""
    logout(request)
    return redirect('learning_logs:index')


def register(request):
    """Faz o cadastro de um novo usuário."""
    # A função de view register() deve exibir um formulário de cadastro em
    # branco quando a página de inscrição for solicitada pela primeira vez e
    # então deve processar o fomulário de cadastro completo quando esse for
    # submetido. Se um cadastro dor bem-sucedido, a função também deverá fazdr
    # o login do novo usuário.
    if request.method != 'POST':
        # Exibe um formulário em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        # Cria uma instância de UserCreationForm com base nos dados submetidos.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():

            # O método save() devolve um objeto para o usuário recém criado,
            # que armazeno em new_user()
            new_user = form.save()

            # Quando as informações do usuário forem salvas, fazemos o seu
            # login, que é um processo de dois passos: chamamos authenticate()
            # com os argumentos new_user.username e a senha.
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])

            # Se o nome do usário e a senha estiverem corretos, o método
            # devolverá um objeto com o usuário autenticado, que armazenamos em
            # authenticated_user. Então chamamos a função login() com os
            # objetos request e authenticated_user, o que criará uma sessão
            # válida para o nome do usuário.
            login(request, authenticated_user)

            # Por fim redirecionamos o usuário para a página inicial
            return HttpResponseRedirect(reverse('learning_logs:index'))
    return render(request, 'users/register.html', {'form': form})
