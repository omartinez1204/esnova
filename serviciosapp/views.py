from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *

# Create your views here.

def login(request):
    matricula=request.GET['matricula']
    contrasenia=request.GET['contrasenia']

    return render(request, 'datos_solicitante.html')

def obtenerDatos_Solicitante(request):
    return render(request,'index.html')
