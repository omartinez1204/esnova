from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def gastos_solicitante(request):
    return render(request, 'Gastos_Solicitante.html')

def datos_solicitante(request):
    return render(request, 'datos_solicitante.html')

def medios_estudiar(request):
    return render(request, 'medios_estudiar.html')

def datos_responsable(request):
    return render(request, 'datos_responsable.html')

def ingreso_familiar(request):
    return render(request, 'ingreso_familiar.html')

def iniciar(request):
    matricula = 'matricula' in request.POST
    contrasenia = 'contrasenia' in request.POST
    #matricula=request.POST['matricula']
    #contrasenia=request.POST['contrasenia']
    usuarios = usuario.objects.all()
    for usuario in usuarios:
        if usuario.matricula == matricula and usuario.contrasenia == contrasenia:
            u = usuario
            context = {
                'usuario':u
            }
            return render(request, 'datos_solicitante.html', context)
    return render(request, 'index.html')

def registrar(request):
    m = 'matricula' in request.POST
    e = 'email' in request.POST
    c = 'contrasenia' in request.POST
    u = usuario(matricula = m, email = e, contrasenia = c)
    u.save()
    return render(request, 'index.html')
