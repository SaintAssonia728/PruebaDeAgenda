from django.urls import path
from . import views
urlpatterns = [
    path("", views.lista_contactos, name="lista_contactos"),
    path("contacto/<int:id>/", views.detalle_contactos, name="detalle_contactos"),
    path("contacto/nuevo/", views.nuevo_contactos, name="nuevo_contactos"),
    path("contacto/editar/<int:id>/", views.editar_contactos, name="editar_contactos"),
    path("contacto/eliminar/<int:id>/", views.eliminar_contactos, name="eliminar_contactos"),
    path("contacto/buscar/", views.buscar_contactos, name="buscar_contactos"),
]
# Le cambiamos el nombre a la vista por el que vamos a llamar en este caso Contactos y le damos un nombre a la url para identificarla mejor en la carpeta templates