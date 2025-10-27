from django import forms # Importamos desde django los formularios para crear formularios basados en los modelos que vamos a usar
from .models import Contactos # Importamos el modelo Contactos que creamos en (models.py) para usarlo en el formulario

class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['nombre', 'correo', 'telefono', 'direccion', 'etiquetas']
        widgets = {
            'etiquetas': forms.CheckboxSelectMultiple(),  # o SelectMultiple
        }
        error_messages = {
            'correo': {
                'unique': "Este correo ya se encuentra en uso, por favor de ingresar otro correo",
                'invalid': "Correo no es valido, debe contener un '@' y un '.' para que sea valido",
            }
        }
    
    def clean_correo(self): # Metodo para limpiar y validar el campo correo
        correo = self.cleaned_data['correo'].strip().lower() # Limpiamos espacios en blanco al inicio y al final y convertimos a minusculas
        return correo

    def clean_telefono(self): # Metodo para limpiar y validar el campo telefono
        telefono = self.cleaned_data['telefono'].strip() # Limpiamos espacios en blanco al inicio y al final
        telefono = telefono.replace(' ', '').replace('-', '')# Eliminamos espacios y guiones
        return telefono 

# Creamos un formulario basado en el modelo Contactos que creamos en (models.py) en model colocamos el modelo que vamos a usar y en fields colocamos los campos que queremos que se muestren en el formulario, en este caso todos los campos del modelo Contactos


