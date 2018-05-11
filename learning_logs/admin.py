from django.contrib import admin
from .models import Topic

# O Django inclui alguns modelos no site de administração de modo automático,
# por exemplo, User e Group, mas os modelos que criei devem ser registrados
# manualmente.
admin.site.register(Topic)
# Esse código importa o modelo que queremos registrar, Topic, e então usa
# admin.site.register() para dizer ao Django que administre nosso modelo por
# meio do site de administração.
