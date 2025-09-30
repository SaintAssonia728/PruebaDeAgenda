from django import forms # Importamos desde django los formularios para crear formularios basados en los modelos que vamos a usar
from .models import Contactos # Importamos el modelo Contactos que creamos en (models.py) para usarlo en el formulario

class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['nombre', 'correo', 'telefono', 'direccion'] # Colocamos estos campos los cuales son los que solicita la agenda de contactos
        
#Creamos un formulario basado en el modelo Contactos que creamos en (models.py) en model colocamos el modelo que vamos a usar y en fields colocamos los campos que queremos que se muestren en el formulario, en este caso todos los campos del modelo Contactos