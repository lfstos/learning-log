from django.urls import path
from . import views

"""Define padrões de URL para learning_logs."""

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Devemos adicionar um argumento topic_id no URL para adicionar uma nova
    # entrada, pois ela deve estar associada a um assunto em particular.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
