from django.shortcuts import render, get_object_or_404, redirect
from .models import Espacio, ServicioAdicional
from .forms import EspacioForm, ServicioAdicionalForm
from django.contrib.auth.decorators import login_required

# ── ESPACIO ──────────────────────────────────────────────────────

@login_required
def espacio_lista(request):
    espacios = Espacio.objects.all()
    return render(request, 'espacios/espacio_lista.html', {'espacios': espacios})

@login_required
def espacio_crear(request):
    form = EspacioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('espacio_lista')
    return render(request, 'espacios/espacio_form.html', {
        'form'  : form,
        'titulo': 'Nuevo Espacio'
    })

@login_required
def espacio_editar(request, pk):
    espacio = get_object_or_404(Espacio, pk=pk)
    form    = EspacioForm(request.POST or None, instance=espacio)
    if form.is_valid():
        form.save()
        return redirect('espacio_lista')
    return render(request, 'espacios/espacio_form.html', {
        'form'  : form,
        'titulo': 'Editar Espacio'
    })

@login_required
def espacio_eliminar(request, pk):
    espacio = get_object_or_404(Espacio, pk=pk)
    if request.method == 'POST':
        espacio.delete()
        return redirect('espacio_lista')
    return render(request, 'espacios/espacio_confirm_delete.html', {'espacio': espacio})

# ── SERVICIO ADICIONAL ───────────────────────────────────────────

@login_required
def servicio_lista(request):
    servicios = ServicioAdicional.objects.all()
    return render(request, 'espacios/servicio_lista.html', {'servicios': servicios})

@login_required
def servicio_crear(request):
    form = ServicioAdicionalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('servicio_lista')
    return render(request, 'espacios/servicio_form.html', {
        'form'  : form,
        'titulo': 'Nuevo Servicio Adicional'
    })

@login_required
def servicio_editar(request, pk):
    servicio = get_object_or_404(ServicioAdicional, pk=pk)
    form     = ServicioAdicionalForm(request.POST or None, instance=servicio)
    if form.is_valid():
        form.save()
        return redirect('servicio_lista')
    return render(request, 'espacios/servicio_form.html', {
        'form'  : form,
        'titulo': 'Editar Servicio Adicional'
    })

@login_required
def servicio_eliminar(request, pk):
    servicio = get_object_or_404(ServicioAdicional, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicio_lista')
    return render(request, 'espacios/servicio_confirm_delete.html', {'servicio': servicio})