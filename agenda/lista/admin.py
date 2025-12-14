from django.contrib import admin
from .models import Contactos, Etiqueta  # Importamos el modelo Contactos y Etiqueta
import csv
from django.http import HttpResponse

@admin.action(description='Exportar seleccionados a CSV')  # Descripción de la acción en el admin
def export_to_csv(modeladmin, request, queryset):  # Acción personalizada para exportar contactos seleccionados a un archivo CSV
    meta = modeladmin.model._meta
    field_names = ['id', 'nombre', 'correo', 'telefono', 'direccion', 'etiquetas']  # Campos que se van a exportar
    response = HttpResponse(content_type='text/csv')  # Tipo de contenido para CSV
    response['Content-Disposition'] = 'attachment; filename=contactos.csv'  # Nombre del archivo descargado
    writer = csv.writer(response)  # Creamos el escritor CSV
    writer.writerow(field_names)  # Escribimos la fila de encabezados
    for obj in queryset:
        etiquetas = ", ".join([t.nombre for t in obj.etiquetas.all()])
        writer.writerow([obj.id, obj.nombre, obj.correo, obj.telefono, obj.direccion, etiquetas])
    return response

@admin.register(Contactos)  # Registramos el modelo Contactos en el admin de django
class ContactosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'etiquetas_display')  # Definimos los campos a mostrar en la lista
    search_fields = ('nombre', 'correo')  # Permite la búsqueda por nombre y correo
    list_filter = ('etiquetas',)  # Filtro por etiquetas
    filter_horizontal = ('etiquetas',)  # Ayuda a editar ManyToMany en admin
    actions = [export_to_csv]  # Habilita la acción personalizada para exportar a CSV

    def etiquetas_display(self, obj):
        return ", ".join([t.nombre for t in obj.etiquetas.all()])  # Muestra las etiquetas de manera legible
    etiquetas_display.short_description = 'Etiquetas'  # Establece el título para las etiquetas en la interfaz admin

@admin.register(Etiqueta)  # Registramos el modelo Etiqueta en el admin de django
class EtiquetaAdmin(admin.ModelAdmin):  # Creamos una clase para personalizar la vista del admin para etiquetas
    list_display = ('nombre',)  # Campos que se van a mostrar en la lista del admin
    search_fields = ('nombre',)  # Permite la búsqueda por nombre de etiqueta