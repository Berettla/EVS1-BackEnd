from django.urls import path
from . import views

app_name = 'musica'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('canciones/', views.canciones, name='canciones'),
]