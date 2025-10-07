from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Reserva
from .forms import ClienteForm, ReservaForm

# Create your views here.

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'reservas/lista_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'reservas/crear_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'reservas/editar_cliente.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('lista_clientes')


# ---- RESERVAS ----
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form})

def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/editar_reserva.html', {'form': form})

def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('lista_reservas')

