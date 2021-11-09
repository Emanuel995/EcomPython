from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Producto

# Vista basada en Clase


class IndexView(TemplateView):
    """ vista basado en clases"""
    template_name = "index.html"

# Vista basada en funcion


def index(request):
    """ vista basado en funciones"""
    return render(request, 'index.html', {})

class ProductoListView(ListView):
    model = Producto
    context_object_name = 'Productos'
    template_name = "listarproductos.html"

