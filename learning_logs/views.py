from django.shortcuts import render, redirect
# render renderiza a resposta de acordo com os dados fornecidos pelas views.
# redirect redireciona para a página selecionada.

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
# Importando o modelo associado que precisamos
from .forms import TopicForm, EntryForm


def index(request):
    """A página inicial de learning_logs."""
    # A função render utiliza dois argumentos, o objeto request original e um
    # template que pode ser usado para construir a página.
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos."""
    topics = Topic.objects.order_by('date_added')
    # Consultamos o banco de dados pedindo os objetos Topic, ordenados de acordo
    # com o atributo date_added. Armazenamos o queryset resultante em topics.
    return render(request, 'learning_logs/topics.html', {'topics': topics})

def topic(request, topic_id):
    """Mostra um assunto e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    # Recuperamos as entradas associadas ao assunto.
    # O sinal de menos na frente de date_added ordena os resultados em
    # ordem inversa
    entries = topic.entry_set.order_by('-date_added')
    return render(request, 'learning_logs/topic.html', {'topic': topic,
                                                        'entries': entries})

def new_topic(request):
    """Adiciona um novo assunto."""
    form = TopicForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('learning_logs:topics')
    else:
        return render(request, 'learning_logs/new_topic.html', {'form': form})

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

        # Definimos o atributo topic de new_entry com o assunto extraído do banco
        # de dados no início da função.
        new_entry.topic = topic

        # Chamamos save sem argumentos, essa instrução salva a entrada no banco
        # de dados com o assunto correto associado.
        new_entry.save()
        return HttpResponseRedirect(reverse('learning_logs:topic',
                                                              args=[topic_id]))
        # Importamos a classe HttpResponseRedirect, que usaremos para
        # redirecionar o leitor de volta à página topics, depois que ele tiver
        # submetido o seu assunto. A função reverse() determina o URL a partir
        # de um padrão de URL nomeado, o que quer dizer que Django gerará o URL
        # quando a página dor solicitada.

    return render(request, 'learning_logs/new_entry.html', {'topic': topic,
                                                            'form': form })
