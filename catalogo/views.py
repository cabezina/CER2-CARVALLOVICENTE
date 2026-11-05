from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Categoria, LugarPatrimonial
from .forms import LugarForm


def home(request):
    return render(request, 'catalogo/home.html')


def catalogo(request):
    lugares = LugarPatrimonial.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/catalogo.html', {
        'lugares': lugares,
        'categorias': categorias,
    })


def lugares_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    lugares = LugarPatrimonial.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/catalogo.html', {
        'lugares': lugares,
        'categorias': categorias,
        'categoria_actual': categoria,
    })


def detalle(request, lugar_id):
    lugar = get_object_or_404(LugarPatrimonial, id=lugar_id)
    return render(request, 'catalogo/detalle.html', {'lugar': lugar})


# ---------- zona restringida ----------

@login_required
def gestion(request):
    lugares = LugarPatrimonial.objects.all()
    return render(request, 'catalogo/gestion.html', {'lugares': lugares})


@login_required
@permission_required('catalogo.add_lugarpatrimonial', raise_exception=True)
def agregar_lugar(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = LugarForm()
    return render(request, 'catalogo/form.html', {'form': form, 'titulo': 'Agregar lugar'})


@login_required
@permission_required('catalogo.change_lugarpatrimonial', raise_exception=True)
def editar_lugar(request, lugar_id):
    lugar = get_object_or_404(LugarPatrimonial, id=lugar_id)
    if request.method == 'POST':
        form = LugarForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = LugarForm(instance=lugar)
    return render(request, 'catalogo/form.html', {'form': form, 'titulo': 'Editar lugar'})
