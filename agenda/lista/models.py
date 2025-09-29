from django.db import models

# Create your models here.

class Contactos(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True) # Usamos EmailField para validar que el correo tenga un formato correcto y unico
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre