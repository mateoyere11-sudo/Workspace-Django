from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'cliente/lista.html',{'clientes':clientes})

@login_required
def crear_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request,'cliente/form.html',{'form':form})

@login_required
def editar_cliente(request,id):
    cliente = get_object_or_404(Cliente,id=id)

    form = ClienteForm(request.POST or None,instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request,'cliente/form.html',{'form':form})

@login_required
def eliminar_cliente(request,id):
    cliente = get_object_or_404(Cliente,id=id)

    cliente.delete()

    return redirect('lista')