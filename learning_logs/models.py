from django.db import models

# Onde criaremos nosso próprios modelos.
# Um modelo diz ao Django como trabalhar com os dados que serão armazenados na
# aplicação. Do ponto de vista do código, um modelo é apenas uma classe; ele tem
# atributos e métodos, assim como todas as classes.

# Criamos uma classe Topic, que herda de Model - uma classe pai incluída em Django,
# que define a funcionalidade básica de um modelo. A classe Topic tem apenas dois
# atributos, text e date_added.

class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo Topic."""
        return self.text
        # Esse atributo é utilizado como default quando ele exibir informações
        # sobre o assunto.

class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""
    topic = models.Foreignkey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name_plural = 'entries'
    # A classe Meta armazena informações extras para administrar um modelo;
    # nesse caso, ela nos permite definir um atributo especial que diz ao Django
    # para usar Entries quando precisar se referir a mais de uma entrada.(Sem
    # isso, Django iria referenciar várias entradas como Entrys).
    
    def __str__(self):
        return self.text[:50] + '...'
