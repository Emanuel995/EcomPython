from django.shortcuts import render
from django.views.generic import TemplateView

# Vista basada en Clase


class IndexView(TemplateView):
    """ vista basado en clases"""
    template_name = "index.html"

# Vista basada en funcion


def index(request):
    """ vista basado en funciones"""
    return render(request, 'index.html', {})
