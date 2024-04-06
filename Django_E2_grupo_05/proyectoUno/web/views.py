from django.shortcuts import render

# Create your views here.

#Daniel: Aqui se llama al archivo html que se va a renderizar (renderizar es mostrar en pantalla), este es el paso 3

def Animales(request):
    return render(request, 'web/Animales.html')

def Armas(request):
    return render(request, 'web/Armas.html')

def Construcciones(request):
    return render(request, 'web/Construcciones.html')

def Consumibles(request):
    return render(request, 'web/Consumibles.html')

def Enemigos(request):
    return render(request, 'web/Enemigos.html')

def Flora(request):
    return render(request, 'web/Flora.html')

def forowiki(request):
    return render(request, 'web/forowiki.html')

def historia(request):
    return render(request, 'web/historia.html')

def inicio_sesion(request):
    return render(request, 'web/inicio_sesion.html')

def Logros(request):
    return render(request, 'web/Logros.html')

def Lugares(request):
    return render(request, 'web/Lugares.html')

def menuprincipal_wiki(request):
    return render(request, 'web/menuprincipal_wiki.html')

def micuentatf(request):
    return render(request, 'web/micuentatf.html')

def recuperarcontra(request):
    return render(request, 'web/recuperarconta.html')

def registrase_wiki(request):
    return render(request, 'web/registrase_wiki.html')