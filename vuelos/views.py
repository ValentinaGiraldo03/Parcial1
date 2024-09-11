from django.shortcuts import render
from .forms import VueloForm

def registrar_vuelos(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vuelos')
    else:
        form = VueloForm()
    return render(request, 'registrar_vuelos.html', {'form': form})
