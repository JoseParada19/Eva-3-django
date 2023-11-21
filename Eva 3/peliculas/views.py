from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm

def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    form = PeliculaForm()
    
    if request.method == "POST":
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_peliculas')
    
    return render(request, 'peliculas/listar_peliculas.html', {'peliculas': peliculas, 'form': form})

def registrar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_peliculas')  
    else:
        form = PeliculaForm()
    
    return render(request, 'peliculas/registrar_pelicula.html', {'form': form})

def editar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('listar_peliculas')
    else:
        form = PeliculaForm(instance=pelicula)
    
    return render(request, 'peliculas/editar_pelicula.html', {'pelicula': pelicula, 'form': form})

def eliminar_pelicula(request, pelicula_id):
    try:
        pelicula = Pelicula.objects.get(id=pelicula_id)
        pelicula.delete()
        return redirect('listar_peliculas')
    except Pelicula.DoesNotExist:
        pass

def vista_principal(request):
    return render(request, 'todo.html')  