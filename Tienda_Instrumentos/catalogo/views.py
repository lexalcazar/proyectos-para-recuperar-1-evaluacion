from django.shortcuts import redirect, render
from .models import Instrumento
from .forms import CategoriaForm, InstrumentoForm, MarcaForm
# Create your views here.



# Vista para la página de inicio
def index(request):
    return render(request, 'catalogo/index.html')


#listado de instrumentos
def listado_instrumentos(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'catalogo/listado_instrumentos.html', {'instrumentos': instrumentos})


# vista para formulario de creación o edición de instrumentos
def formulario_instrumento(request, id=None):
    form= InstrumentoForm(request.POST or None, instance=Instrumento.objects.get(id=id) if id else None)
    if form.is_valid():
        form.save()
        return redirect('listado_instrumentos')
    return render(request, 'catalogo/formulario_instrumento.html', {'form': form})

# vista formulario para crear categorias
def nuevo_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'catalogo/formulario_categoria.html', {'form': form})
# vista formulario para crear marcas
def nuevo_marca(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'catalogo/formulario_marca.html', {'form': form})