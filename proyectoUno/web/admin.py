from django.contrib import admin
#importar los modelos:
from .models import Tipo_usuario,Usuario

# Register your models here.
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
#Dennisse: aquí agregamos los modelos que queremos editar desde el panel de administracion
# Register your models here.
