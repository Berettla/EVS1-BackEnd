from django.urls import path
from . import views

app_name = 'juegos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista_juegos, name='lista_juegos'),
]