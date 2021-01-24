from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *
def index(request):

    return render(request, 'index.html')
def gastos_solicitante(request):
    return render(request, 'Gastos_Solicitante.html')

def datos_solicitante(request):
    return render(request, 'datos_solicitante.html')

def medios_estudiar(request):
    return render(request, 'medios_estudiar.html')

def datos_responsable(request):
    return render(request, 'datos_responsable.html')
