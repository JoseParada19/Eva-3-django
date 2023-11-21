from django.shortcuts import render, redirect
from .models import Entrada
from .forms import EntradaForm

def listar_entradas(request):
    entradas = Entrada.objects.all()
    form = EntradaForm()
    
    if request.method == "POST":
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_entradas')
    
    return render(request, 'entrada/listar_entradas.html', {'entradas': entradas, 'form': form})

def registrar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_entradas')  
    else:
        form = EntradaForm()
    
    return render(request, 'entrada/registrar_entrada.html', {'form': form})

def editar_entrada(request, id):
    entrada = Entrada.objects.get(id=id)
    
    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('listar_entradas')
    else:
        form = EntradaForm(instance=entrada)
    
    return render(request, 'entrada/editar_entrada.html', {'entrada': entrada, 'form': form})

def eliminar_entrada(request, entrada_id):
    try:
        entrada = Entrada.objects.get(id=entrada_id)
        entrada.delete()
        return redirect('listar_entradas')
    except Entrada.DoesNotExist:
        pass


def pagina_principal(request):
    return render(request, 'todo.html')


