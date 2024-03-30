from django.urls import path #Daniel: Importamos la funcion path
from .views import home #Daniel: Importamos la funcion home del archivo views.py

urlpatterns = [
    path('', home, name='home'),
] #Daniel: Aqui se crea una lista de urls que se van a utilizar en el proyecto, este el paso 3

