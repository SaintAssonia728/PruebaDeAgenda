from django.shortcuts import render, get_object_or_404, redirect
from .models import Contactos
from django.db.models import Q # Importamos Q para poder hacer consultas las cuales la vamos a usar para hacer busquedas
from .forms import ContactosForm # Importamos los modelos y los formularios que vamos a usar en las vistas

# Create your views here.

def lista_contactos(request): # Creamos La vista de lista de contactos donde se podran mostrar todos los contactos que se han agregado a la agenda usaremos (return) para regresar una respuesta http y usaremos (render) para renderizar una plantilla 
    query = request.GET.get('q', '')
    if query:
        contactos = Contactos.objects.filter(nombre__icontains=query) # Esto busca en la bas
    else:
        contactos = Contactos.objects.all()
    return render(request, 'lista/lista_contactos.html', {'contactos': contactos, 'query': query})

def detalle_contactos(request, id): # Creamos la vista de detalle de contactos donde se podran ver los detalles de cada contacto 
    contacto = get_object_or_404(Contactos, id=id)
    return render(request, 'lista/detalle_contactos.html', {'contactos': contacto})

def nuevo_contactos(request): # Usamos el metodo Post para crear un nuevo contacto usando que creamos en (forms.py) lo usamos para crear un formulario basado en el modelo Contactos que creamos en (models.py)
    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid(): # Validamos que el formulario sea valido
            form.save() # Guardamos el formulario
            return redirect('lista_contactos') # Redirigimos a la vista de lista de contactos despues de guardar el formulario
    else:
        form = ContactosForm()
    return render(request, 'lista/nuevo_contactos.html', {'form': form})

def editar_contactos(request, id): # Usamos el metodo Post para editar un contacto que ya existe 
    contacto = get_object_or_404(Contactos, id=id)
    if request.method == 'POST': 
        form = ContactosForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos') # Denuevo lo validamos y lo guardamos y redirigimos a la vista de lista de contactos
    else:
        form = ContactosForm(instance=contacto) 
    return render(request, 'lista/editar_contactos.html', {'form': form})

def eliminar_contactos(request, id): # Creamos la vista para eliminar un contacto usando el metodo Post
    contacto = get_object_or_404(Contactos, id=id)
    if request.method == 'POST':
        contacto.delete() # Si el metodo es Post eliminamos el contacto y luego redirigimos a la vista de lista de contactos
        return redirect('lista_contactos')
    return render(request, 'lista/eliminar_contactos.html', {'contactos': contacto})

def buscar_contactos(request): # Creamos la vista para buscar contactos solo por nombre
    query = request.GET.get('q', '') # Obtenemos el valor del campo de busqueda (q) y quitamos espacios
    resultados = []
    if query:
        resultados = Contactos.objects.filter(nombre__icontains=query)
    # Si el campo está vacío, resultados será una lista vacía y no se mostrará nada
    return render(request, 'lista/buscar_contactos.html', {'resultados': resultados, 'query': query})

