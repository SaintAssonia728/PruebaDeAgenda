from django.shortcuts import render, get_object_or_404, redirect
from .models import Contactos
from .forms import ContactosForm # Importamos los modelos y los formularios que vamos a usar en las vistas

# Create your views here.

def lista_contactos(request): 
    contactos = Contactos.objects.all()
    return render(request, 'lista/lista_contactos.html', {'contactos': contactos})

def detalle_contactos(request, id):
    contacto = get_object_or_404(Contactos, id=id)
    return render(request, 'lista/detalle_contactos.html', {'contactos': contacto})

def nuevo_contactos(request): # Usamos el metodo Post 
    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactosForm()
    return render(request, 'lista/nuevo_contactos.html', {'form': form})

def editar_contactos(request, id):
    contacto = get_object_or_404(Contactos, id=id)
    if request.method == 'POST':
        form = ContactosForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactosForm(instance=contacto)
    return render(request, 'lista/editar_contactos.html', {'form': form})

def eliminar_contactos(request, id):
    contacto = get_object_or_404(Contactos, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'lista/eliminar_contactos.html', {'contactos': contacto})


def detalle_contactos(request, id):
    contacto = get_object_or_404(Contactos, id=id)
    return render(request, 'lista/detalle_contactos.html', {'contactos': contacto})

def nuevo_contactos(request):
    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactosForm()
    return render(request, 'lista/nuevo_contactos.html', {'form': form})

def editar_contactos(request, id):
    contacto = get_object_or_404(Contactos, id=id)
    if request.method == 'POST':
        form = ContactosForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactosForm(instance=contacto)
    return render(request, 'lista/editar_contactos.html', {'form': form})

def eliminar_contactos(request, id):
    contacto = get_object_or_404(Contactos, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'lista/eliminar_contactos.html', {'contactos': contacto})
 
