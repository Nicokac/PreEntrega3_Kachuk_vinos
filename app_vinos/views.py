from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Vino, Preferencia, Recomendacion
from .forms import PreferenciaForm, BuscarRecomendacionForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

#@login_required
def agregar_preferencia(request):
    try:
        preferencia = Preferencia.objects.get(usuario=request.user)
    except Preferencia.DoesNotExist:
        preferencia = None

    if request.method == 'POST':
        form = PreferenciaForm(request.POST, instance=preferencia)
        if form.is_valid():
            preferencia = form.save(commit=False)
            preferencia.usuario = request.user
            preferencia.save()
            return redirect('recomendar_vinos')
    else:
        form = PreferenciaForm(instance=preferencia)

    return render(request, 'agregar_preferencias.html', {'form': form})

#@login_required
def recomendar_vinos(request):
    preferencia = Preferencia.objects.get(usuario=request.user)
    vinos_recomendados = Vino.objects.filter(
        tipo=preferencia.tipo_vino,
        anio__gte=preferencia.anio_minimo,
        anio__lte=preferencia.anio_maximo
    )

    for vino in vinos_recomendados:
        Recomendacion.objects.get_or_create(usuario=request.user, vino=vino)

    return render(request, 'recomendar_vinos.html', {'vinos': vinos_recomendados})
