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

def dependencia(request):
    return render(request, 'dependencias.html')

def datos_solicitante(request):
    return render(request, 'datos_solicitante.html')

def medios_estudiar(request):
    return render(request, 'medios_estudiar.html')

def datos_responsable(request):
    return render(request, 'datos_responsable.html')

def ingreso_familiar(request):
    return render(request, 'ingreso_familiar.html')

def iniciar(request):
    matricula=request.POST['matricula']
    contrasenia=request.POST['contrasenia']
    usuarios = Usuario.objects.all()
    for user in usuarios:
        if user.matricula == matricula and user.contrasenia == contrasenia:
            u = user
            context = {
                'usuario':u,
            }
            return render(request, 'datos_solicitante.html', context)
    return render(request, 'index.html')

def registrar(request):
    m=request.POST['matricula']
    e=request.POST['email']
    c=request.POST['contrasenia']
    u = usuario(matricula = m, email = e, contrasenia = c)
    u.save()
    return render(request, 'index.html')
