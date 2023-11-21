from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def listar_clientes(request):
    clientes = Cliente.objects.all()
    form = ClienteForm()
    
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes, 'form': form})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')  
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/registrar_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'clientes/editar_cliente.html', {'cliente': cliente, 'form': form})

def eliminar_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.delete()
        return redirect('listar_clientes')
    except Cliente.DoesNotExist:
        pass

def pagina_principal(request):
    return render(request, 'todo.html')
