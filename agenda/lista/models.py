from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Etiqueta(models.Model): # Modelo para las etiquetas de los contactos
    nombre = models.CharField(max_length=50, unique=True) # Usamos CharField para el nombre de la etiqueta, con un maximo de 50 caracteres y unico para evitar etiquetas duplicadas
    
    def __str__(self):
        return self.nombre
    
telefono_validator = RegexValidator(
    regex=r'^\+?\d{7,15}$',
    message='Ingrese un teléfono válido (solo dígitos, opcional +, entre 7 y 15 dígitos).'
)

class Contactos(models.Model):
    nombre = models.CharField(max_length=100) 
    correo = models.EmailField(unique=True) # Usamos EmailField para validar que el correo tenga un formato correcto y unico
    telefono = models.CharField(max_length=20, validators=[telefono_validator])
    direccion = models.CharField(max_length=255)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name='contactos')

    def __str__(self):
        return self.nombre

# Para El Nombre, Telefono, Direccion usaremos (Charfield) ya que con este tipo de modelo o dato en django para el nombre es perfecto sobre todo por la cantidad que se almacena al igual que para la direccion y el telefono, en el caso del correo usaremos (EmailField) ya que este tipo de dato valida que el formato del correo sea correcto y unico al usarlo genera mensajes automaticamenta por django el cual se puede cambiar al hacer uso de (mensaje_error)