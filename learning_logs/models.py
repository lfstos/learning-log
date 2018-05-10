from django.db import models

"""
Onde criaremos nosso próprios modelos.
Um modelo diz ao Django como trabalhar com os dados que serão armazenados na
aplicação. Do ponto de vista do código, um modelo é apenas uma classe; ele tem
atributos e métodos, assim como todas as classes.

Criamos uma classe Topic, que herda de Model - uma classe pai incluída em Django,
que define a funcionalidade básica de um modelo. A classe Topic tem apenas dois
atributos, text e date_added.
"""

class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text
