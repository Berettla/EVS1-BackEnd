from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'juegos/inicio.html')

def lista_juegos(request):
    return render(request, 'juegos/lista_juegos.html')