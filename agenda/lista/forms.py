from django import forms
from .models import Contactos

class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['nombre', 'correo', 'telefono', 'direccion'] # Colocamos estos campos los cuales son los que solicita la agenda de contactos
        
