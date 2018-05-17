from django import forms

# Importa os Modelos Topic e Entry para criar automaticamente os formulários.
from .models import Topic, Entry

# Definimos uma classe chamada TopicForm que herda de forms.ModelForm
class TopicForm(forms.ModelForm):
    # A versão mais simples de um ModelForm é constituída de uma classe Meta
    class Meta:
        # Diz ao Django em qual modelo o formulário deve se basear.
        # Criamos o formulário a partir do modelo Topic.
        model = Topic
        # Quais os campos devem ser incluídos nesse formulário.
        fields=['text']
        labels = {'text': ''}

# Definimos a classe chamada EntryForm que herda de forms.ModelForm
class EntryForm(forms.ModelForm):
    # A versão mais simples de um ModelForm é constituída de uma classe Meta
    class Meta:
        # Diz ao Django em qual modelo o formulário deve se basear.
        model = Entry
        # Quais os campos que serão inclusos nesses formulários
        fields = ['text']
        labels={'text': ''}
        # Um widget é um elemento de formulário HTML, por exemplo, uma caixa de texto de
        # uma única linha, uma área de texto com várias linhas ou uma lista suspensa.
        # Ao incluir o atirbuto widgets, podemos sobrescrever as opções default de
        # widgets de Django. Ao usar um elemento forms.Textarea, estamos personalizando
        # o widget de entrada para o campo 'text' de modo que a área de texto tenha 80
        # colunas, em vez de usar o default de 40.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
