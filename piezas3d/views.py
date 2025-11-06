from django.shortcuts import render, redirect, get_object_or_404
from .models import Pieza3D, Categoria, Material
from .forms import Pieza3DForm, CategoriaForm, MaterialForm
from django.core.paginator import Paginator

def inicio(request):
    return render(request, 'piezas3d/inicio.html')

def listar_piezas(request):
    q = request.GET.get('q','')
    piezas = Pieza3D.objects.all().order_by('-fecha_creacion')
    if q:
        piezas = piezas.filter(nombre__icontains=q)
    paginator = Paginator(piezas, 8)
    page = request.GET.get('page')
    piezas_p = paginator.get_page(page)
    return render(request, 'piezas3d/listar_piezas.html', {'piezas': piezas_p, 'q': q})

def crear_pieza(request):
    if request.method == 'POST':
        form = Pieza3DForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_piezas')
    else:
        form = Pieza3DForm()
    return render(request, 'piezas3d/form_pieza.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_pieza')
    else:
        form = CategoriaForm()
    return render(request, 'piezas3d/form_categoria.html', {'form': form})

def crear_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_pieza')
    else:
        form = MaterialForm()
    return render(request, 'piezas3d/form_material.html', {'form': form})
