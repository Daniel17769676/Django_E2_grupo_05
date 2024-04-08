from django.db import models

# Create your models here.
#Vamos a crear dos tablas, una para el tipo de usuario y otra para la información del usuario

#modelo para tipo_usuario
class Tipo_usuario(models.Model):
    ID_TIPO_USUARIO = models.IntegerField(primary_key=True, verbose_name='Id tipo usuario')
    DESCRIPCION = models.CharField(max_length=15, verbose_name='Nombre tipo usuario')

    def __str__(self):
        return self.DESCRIPCION
    
#modelo para usuario
class Usuario(models.Model):
    ID_USUARIO = models.IntegerField(primary_key=True, verbose_name='Id usuario')
    ID_TIPO_USUARIO = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE, verbose_name='Tipo de usuario')
    NOMBRE = models.CharField(max_length=50, verbose_name='Nombre del usuario')
    CORREO = models.EmailField(verbose_name='Correo electronico')
    PASSWORD = models.CharField(max_length=50, verbose_name='Contraseña')
    def __str__(self):
        return self.NOMBRE


