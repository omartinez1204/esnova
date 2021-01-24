from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *

# Create your views here.

def login(request):
<<<<<<< HEAD
    matricula=request.GET['matricula']
    contrasenia=request.GET['contrasenia']

    return render(request, 'datos_solicitante.html')

def obtenerDatos_Solicitante(request):
    return render(request,'index.html')
=======
    matricula=request.POST['matricula']
    contrasenia=request.POST['contrasenia']

    usuarios = usuario.objects.all()
    for usuario in usuarios:
        if usuario.matricula == matricula and usuario.contrasenia == contrasenia
            u = usuario
    context = {
        'usuario':u
    }
    return render(request, 'datos_solicitante.html', context)

def registrar(request):
    u = usuario(request.POST['matricula'], request.POST['contrasenia'], request.POST['email'])
    u.save()
    return render(request, 'index.html')
>>>>>>> d46141bbddd3e5bfab1f4355505acb3836c13e96
