from django.contrib import admin
from .models import Topic

# Modelo que o Django inclui automaticamente no site de administração 
admin.site.register(Topic)
