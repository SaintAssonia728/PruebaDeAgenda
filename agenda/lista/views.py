from django.shortcuts import render, get_object_or_404, redirect
from .models import Contactos
from django.http import JsonResponse
from django.db.models import Q # Importamos Q para poder hacer consultas las cuales la vamos a usar para hacer busquedas
from .forms import ContactosForm # Importamos los modelos y los formularios que vamos a usar en las vistas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer, ContactosSerializer

# Es de ejemplo para un endpoint protegido que requiere autenticacion
from django.contrib.auth.decorators import login_required
@login_required
def custom_endpoint(request):
    return JsonResponse({
        "secretos": "secretos solo para usuarios autenticados"
    })


class ContactosViewSet(viewsets.ModelViewSet):
    queryset = Contactos.objects.all().order_by("nombre")
    serializer_class = ContactosSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# Create your views here.

def lista_contactos(request): # Creamos La vista de lista de contactos donde se podran mostrar todos los contactos que se han agregado a la agenda usaremos (return) para regresar una respuesta http y usaremos (render) para renderizar una plantilla 
    query = request.GET.get('q', '')
    if query:
        contactos_qs = Contactos.objects.filter(nombre__icontains=query) # Esto busca en la base
    else:
        contactos_qs = Contactos.objects.all()

    # Paginación: 10 contactos por página
    paginator = Paginator(contactos_qs, 10)
    page = request.GET.get('page')
    try:
        contactos = paginator.page(page)
    except PageNotAnInteger:
        contactos = paginator.page(1)
    except EmptyPage:
        contactos = paginator.page(paginator.num_pages)

    context = {
        'contactos': contactos,
        'query': query,
        'is_paginated': contactos.has_other_pages(),
        'page_obj': contactos,
    }
    return render(request, 'lista/lista_contactos.html', context)

def detalle_contactos(request, id): # Creamos la vista de detalle de contactos donde se podran ver los detalles de cada contacto 
    contacto = get_object_or_404(Contactos, id=id)
    return render(request, 'lista/detalle_contactos.html', {'contactos': contacto})

def nuevo_contactos(request): # Usamos el metodo Post para crear un nuevo contacto usando que creamos en (forms.py) lo usamos para crear un formulario basado en el modelo Contactos que creamos en (models.py)
    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid(): # Validamos que el formulario sea valido
            form.save() # Guardamos el formulario
            messages.success(request, 'Contacto creado correctamente.')
            return redirect('lista_contactos') # Redirigimos a la vista de lista de contactos despues de guardar el formulario
        else:
            messages.error(request, 'Hubo errores en el formulario. Verifique los campos.')
    else:
        form = ContactosForm()
    return render(request, 'lista/nuevo_contactos.html', {'form': form})

def editar_contactos(request, id): # Usamos el metodo Post para editar un contacto que ya existe 
    contacto = get_object_or_404(Contactos, id=id)
    if request.method == 'POST': 
        form = ContactosForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contacto actualizado correctamente.')
            return redirect('lista_contactos') # Denuevo lo validamos y lo guardamos y redirigimos a la vista de lista de contactos
        else:
            messages.error(request, 'Hubo errores al actualizar el contacto. Revise los campos.')
    else:
        form = ContactosForm(instance=contacto) 
    return render(request, 'lista/editar_contactos.html', {'form': form})

def eliminar_contactos(request, id): # Creamos la vista para eliminar un contacto usando el metodo Post
    contacto = get_object_or_404(Contactos, id=id)
    if request.method == 'POST':
        contacto.delete() # Si el metodo es Post eliminamos el contacto y luego redirigimos a la vista de lista de contactos
        messages.success(request, 'Contacto eliminado correctamente.')
        return redirect('lista_contactos')
    return render(request, 'lista/eliminar_contactos.html', {'contactos': contacto})

def buscar_contactos(request): # Creamos la vista para buscar contactos solo por nombre
    query = request.GET.get('q', '') # Obtenemos el valor del campo de busqueda (q) y quitamos espacios
    resultados = []
    if query:
        resultados = Contactos.objects.filter(nombre__icontains=query)
    # Si el campo está vacío, resultados será una lista vacía y no se mostrará nada
    return render(request, 'lista/buscar_contactos.html', {'resultados': resultados, 'query': query})