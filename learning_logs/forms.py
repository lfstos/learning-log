from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields=['text']
        labels = {'text': ''}
# Inicialmente importamos o módulo forms e o modelo Topic.
# Definimos uma classe chamada TopicForm que herda de forms.ModelForm
# A versão mais simples de um ModelForm é constituída de uma classe Meta
# aninhada que diz ao Django em qual modelo o formulário deve se basear
# e quais campos devem ser incluídos nesse formulário.

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
# A classe herda de forms.ModelForm e tem uma classe Meta aninhada que lista o
# modelo no qual ela está baseada e o campo a ser incluído no formulário.
# Um widget é um elemento de formulário HTML, por exemplo, uma caixa de texto de
# uma única linha, uma área de texto com várias linhas ou uma lista suspensa.
# Ao incluir o atirbuto widgets, podemos sobrescrever as opções default de
# widgets de Django. Ao usar um elemento forms.Textarea, estamos personalizando
# o widget de entrada para o campo 'text' de modo que a área de texto tenha 80
# colunas, em vez de usar o default de 40.
