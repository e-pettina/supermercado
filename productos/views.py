# Create your views here.

from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'productos/lista.html', {'productos': productos})

def cargar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('accion') == 'guardar_y_nuevo':
                return redirect('cargar_producto')
            else:
                return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'productos/cargar.html', {'form': form})
