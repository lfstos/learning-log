# render renderiza a resposta de acordo com os dados fornecidos pelas views.
# redirect redireciona para a página selecionada.
# Request é um objeto de requisição.
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

# Importando o modelo associado que precisamos
from .models import Topic, Entry

# Importamos os formulários
from .forms import TopicForm, EntryForm

# @login_required
# Um decorador é uma diretiva colocada imediatamente antes da definição de uma
# função, que Python aplica a ela antes que seja executada a fim de alterar o
# modo como essa funçao se comporta
from django.contrib.auth.decorators import login_required


def index(request):
    """A página inicial de learning_logs."""
    # A função render utiliza dois argumentos, o objeto request original e um
    # template que pode ser usado para construir a página.
    return render(request, 'learning_logs/index.html')

# Aplicamos login_required() como um decorador da função de view topics()
# prefixando login_required com o símbolo @ para que Python saiba que deve
# executar o código em login_required() antes do código em topics().
# O código em login_required() verifica se um usuário está logado, e Django
# executará o código em topics() somente em caso afirmativo. Se não estiver
# logado, o usuário será redirecinado para a página de login.
# Para fazer esse redirecionamento funcionar, devemos modificar settings.py
# para que o Django saiba em que local pode encontrar a página login


@login_required
def topics(request):
    """Mostra todos os assuntos."""
    # Quando um usuário está logado, o objeto de requisição tem um atributo
    # request.user definido, que armazena informações sobre o usuário.
    # O fragmento de código Toopic.objects.filter(owner=request.user) diz ao
    # Django para recuperar apenas os objetos Topic do banco de dados cujo
    # atributo owner seja igual ao usuário atual. Como não estamos mudando o
    # modo como os assuntos são exibido, não é necessário alterar p template da
    # página de assuntos.
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # Consultamos o banco de dados pedindo os objetos Topic, ordenados de
    # acordo com o atributo date_added. Armazenamos o queryset resultante em
    # topics.
    return render(request, 'learning_logs/topics.html', {'topics': topics})


@login_required
def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    # Garante que o assunto pertence ao usuário atual.

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    return render(request, 'learning_logs/topic.html', {'topic': topic,
                                                        'entries': entries})

# A função de new_topic() deve tratar duas situações diferentes:
# Requisições iniciais para a página new_topic(caso em que o formulário em
# branco deverá ser mostrado) e o processamento de qualquer dado submetido
# no formulário que será redirecionado para learning_logs:topics.


@login_required
def new_topic(request):
    """Adiciona um novo assunto."""
    form = TopicForm(request.POST or None)
    # Não podemos salvar as informações submetidas no banco de dados antes de
    # verificar se são válidas. A função is_valid() verifica se todos os campos
    # necessários são preenchidos(todos os campos em um formulário são
    # obrigatórios por padrão) e se os dados fornecidos são do tipo esperado
    # para o campo.
    if form.is_valid():
        # Se tudo estiver válido, chamamos save(), que grava os dados do
        # formulário no banco de dados.
        # Quando chamamos form.save() pela primeira vez, passamos o argumento
        # commit=False poruqe precisamos modificar o novo assunto antes de
        # salválo no banco de dados. Então definimos o atributo owner do novo
        # assunto com o usuário atual. Por fim, chamamos sabe() na instância do
        # assunto que acabou de ser definido. Agora o assunto tem todos os
        # dados necessários e será salvo com sucesso.
        new_topic = form.save(commit=False)
        new_topic.owner = request.user
        new_topic.save()
        return redirect('learning_logs:topics')
    # Criamos uma instância de TopicForm, armazenamos essa instância em uma
    # variável form e enviamos o formulario para o template no dicionário de
    # contexto. Como não incluímos nenhum argumento ao instânciar TopicForm,
    # o Django cria um formulário em branco que o usuário poderá preencher.
    form = TopicForm()
    # Caso seja a primeira requisição, para criação de um novo topic.
    return render(request, 'learning_logs/new_topic.html', {'form': form})


@login_required
def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""
    # Recuperando o assunto que desejamos criar a entrada.
    topic = Topic.objects.get(id=topic_id)

    # Criamos uma instância de EntryForm preenchida com os dados de POST do
    # objeto request, e verificamos se o método da requisição é POST ou GET.
    form = EntryForm(request.POST or None)

    # Verificamos se o formulário é válido, se for, devemos definir o atributo
    # topic do objeto de entrada antes de salvá-lo no banco de dados.
    if form.is_valid():

        # Quando chamamos save(), incluímos o argumento commit=False para dizer
        # ao Django que crie um novo objeto de entrada e armazene em new_entry
        # sem salvá-lo no banco de dados por enquanto.
        new_entry = form.save(commit=False)

        # Definimos o atributo topic de new_entry com o assunto extraído do
        # banco de dados no início da função.
        new_entry.topic = topic

        # Chamamos save sem argumentos, essa instrução salva a entrada no banco
        # de dados com o assunto associado.
        new_entry.save()
        return HttpResponseRedirect(reverse('learning_logs:topic',
                                             args=[topic_id]))
        # Importamos a classe HttpResponseRedirect, que usaremos para
        # redirecionar o leitor de volta à página topics, depois que ele tiver
        # submetido o seu assunto. A função reverse() determina o URL a partir
        # de um padrão de URL nomeado, o que quer dizer que Django gerará o URL
        # quando a página dor solicitada.

    return render(request, 'learning_logs/new_entry.html', {'topic': topic,
                                                            'form': form})


@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente."""
    # Adquirimos o objeto da entrada que o usuário quer editar e o assunto
    # associado a essa entrada.
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Criamos uma instância de EntryForm com o argumento instance=entry
        # Esse argumento diz ao Django para criar o formulário previamente
        # preenchido com informações do objeto de entrada existente. O usuário
        # verá os dados existentes e poderá editá-los
        form = EntryForm(instance=entry)
    else:
        # Ao processar uma requisição POST, passamos os argumentos
        # instance=entry e data=request.POST para dizer ao Django que crie uma
        # instância de formulário baseada nas informações associadas ao objeto
        # de entrada existente, atualizando com qualquer dado relevante de
        # request.POST.
        form = EntryForm(instance=entry, data=request.POST)

        # Se veio POST, validamos a requisição para ver se está tudo certo.
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                        args=[topic.id]))
    return render(request, 'learning_logs/edit_entry.html', {'entry': entry,
                                                             'topic': topic,
                                                             'form': form})
