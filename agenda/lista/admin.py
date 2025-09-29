from django.contrib import admin
from .models import Contactos # Importamos el modelo Contactos el cual creamos para que despues aparezca y se vea reflejado en el panel de admin

# Register your models here.

admin.site.register(Contactos)