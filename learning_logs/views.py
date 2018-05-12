from django.shortcuts import render

# render renderiza a resposta de acordo com os dados fornecidos pelas views.

# Create your views here.

def index(request):
    """A página inicial de learning_logs."""
    # A função render utiliza dois argumentos, o objeto request original e um
    # template que pode ser usado para construir a página.
    return render(request, 'learning_logs/index.html')
