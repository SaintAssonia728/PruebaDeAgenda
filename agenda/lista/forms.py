from django import forms # Importamos desde django los formularios para crear formularios basados en los modelos que vamos a usar
from .models import Contactos # Importamos el modelo Contactos que creamos en (models.py) para usarlo en el formulario

class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['nombre', 'correo', 'telefono', 'direccion'] # Colocamos estos campos los cuales son los que solicita la agenda de contactos
        error_messages = { #Con (error_messages) lo usamos para poder personalizar los mensajes de error que genera django automaticamente de por si django al no colocar el formato correcto en el correo muestra un mensaje de que falta el @ y el .com y si lo colocamos mal saldra uno hecho por django
            'correo': {
                'unique': "Este correo ya se encuentra en uso por favor ingresar otro correo", # Personalizamos el mensaje de error que genera django automaticamente al usar (EmailField) en el modelo Contactos en el caso de que el correo ya exista
        }
    }

# Creamos un formulario basado en el modelo Contactos que creamos en (models.py) en model colocamos el modelo que vamos a usar y en fields colocamos los campos que queremos que se muestren en el formulario, en este caso todos los campos del modelo Contactos

