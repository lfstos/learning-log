from django.shortcuts import render
# render renderiza a resposta de acordo com os dados fornecidos pelas views.

from .models import Topic
# Importando o modelo associado que precisamos

# Create your views here.

def index(request):
    """A página inicial de learning_logs."""
    # A função render utiliza dois argumentos, o objeto request original e um
    # template que pode ser usado para construir a página.
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos."""
    topics = Topic.objects.order_by('date_added')
    # Consultamos o banco de dados pedindo os objetos Topic, ordenados de acprdo
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
