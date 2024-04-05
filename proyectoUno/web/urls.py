from django.urls import path #Daniel: Importamos la funcion path
from .views import Animales, Armas, Construcciones, Consumibles,Enemigos, Flora, forowiki, historia,inicio_sesion, Logros, Lugares,menuprincipal_wiki, micuentatf, recuperarcontra,registrase_wiki #Daniel: Importamos la funcion home del archivo views.py

urlpatterns = [
   
    path('animales',Animales, name="Animales"),
    path('armas',Armas,name="Armas"),
    path('construcciones',Construcciones,name="Construcciones"),
    path('consumibles',Consumibles,name="Consumibles"),
    path('enemigos',Enemigos,name="Enemigos"),
    path('flora',Flora,name="Flora"),
    path('forowiki',forowiki,name="forowiki"),
    path('historia',historia,name="historia"),
    path('inicio_sesion',inicio_sesion,name="inicio_sesion"),
    path('logros',Logros,name="Logros"),
    path('lugares',Lugares,name="Lugares"),
    path('menuprincipal',menuprincipal_wiki,name="menuprincipal"),
    path('micuentatf',micuentatf,name="micuentatf"),
    path('recuperarcontra',recuperarcontra,name="recuperarcontra"),
    path('registrase',registrase_wiki,name="registrase"),

] #Daniel: Aqui se crea una lista de urls que se van a utilizar en el proyecto, este el paso 3

