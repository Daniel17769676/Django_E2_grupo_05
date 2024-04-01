from django.urls import path #Daniel: Importamos la funcion path
from .views import (Animales, Armas, Construcciones, Consumibles,
                    Enemigos, Flora, forowiki, historia,
                    inicio_sesion, Logros, Lugares,
                    menuprincipal_wiki, micuentatf, recuperarcontra,
                    registrase_wiki) #Daniel: Importamos la funcion home del archivo views.py

urlpatterns = [
   
    path('',Animales, name="Animales"),
    path('',Armas,name="Armas"),
    path('',Construcciones,name="Construcciones"),
    path('',Consumibles,name="Consumibles"),
    path('',Enemigos,name="Enemigos"),
    path('',Flora,name="Flora"),
    path('',forowiki,name="forowiki"),
    path('',historia,name="historia"),
    path('',inicio_sesion,name="inicio_sesion"),
    path('',Logros,name="Logros"),
    path('',Lugares,name="Lugares"),
    path('',menuprincipal_wiki,name="menuprincipal"),
    path('',micuentatf,name="micuentatf"),
    path('',recuperarcontra,name="recuperarcontra"),
    path('',registrase_wiki,name="registrase"),

] #Daniel: Aqui se crea una lista de urls que se van a utilizar en el proyecto, este el paso 3

