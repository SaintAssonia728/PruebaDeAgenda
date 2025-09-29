from django.db import models

# Create your models here.

class Contactos(models.Model):
    nombre = models.CharField(max_length=100) 
    correo = models.EmailField(unique=True) # Usamos EmailField para validar que el correo tenga un formato correcto y unico al usarlo genera mensajes automaticamenta por django el cual lo podemos cambiar al usar con (mensaje_error)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    #Para El Nombre, Telefono, Direccion usaremos (Charfield) ya que con este tipo de modelo o dato en djangio para ekl nombre es perfecto sobre todo por la cantidad que se almcena 