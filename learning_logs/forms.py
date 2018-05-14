from django import forms
from .models import Topic

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
