from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'musica/inicio.html')

def canciones(request):
    return render(request, 'musica/canciones.html')