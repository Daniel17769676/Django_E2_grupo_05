from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'web/menuprincipal_wiki.html')#Daniel: Aqui se llama al archivo html que se va a renderizar (renderizar es mostrar en pantalla), este es el paso 3
