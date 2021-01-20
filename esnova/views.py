from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *
def index(request):
    articulos = Articulo.objects.all()
    context = {
        'articulos': articulos
    }
    return render(request, 'index.html', context)
