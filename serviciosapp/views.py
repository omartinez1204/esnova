from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *
from datetime import datetime,date

# Create your views here.

def login(request):
    matricula=request.POST['matricula']
    contrasenia=request.POST['contrasenia']
    usuarios = usuario.objects.all()
    for usuario in usuarios:
        if usuario.matricula == matricula and usuario.contrasenia == contrasenia:
            u = usuario
    context = {
        'usuario':u
    }
    return render(request, 'datos_solicitante.html', context)

#def registrar(request):
#    u = usuario(request.POST['matricula'], request.POST['contrasenia'], request.POST['email'])
#    u.save()
#    return render(request, 'index.html')


def obtenerDatos_Solicitante(request):

    if request.POST['solicita_beca_alimentaria'] == 'si':
        variable = True
    else :
        variable = False
    if request.POST['residencia_distinta'] == 'si':
        variable2 = True
    else :
        variable2 = False
    if request.POST['sexo'] == "M":
        variable3 = True
    else :
        variable3 = False

    datosPersonalesModel = datosPersonales(fecha = date.today(), solicita_beca_alimentaria= bool(variable),
    ap_paterno=request.POST['apellido_paterno'], ap_materno = request.POST['apellido_materno'], nombre = request.POST['nombre'],
    sexo = variable3, edad = request.POST['edad'], estado_civil = request.POST['estado_civil'], carrera =request.POST['carrera'],
    semestre = request.POST['semestre'],grupo = request.POST['grupo'],telefono = request.POST['celular'], otro_idiona =  request.POST['otro_idioma'],
    residencia_distinta = variable2 , calle =  request.POST['calle'], numero = request.POST['numero_calle'],
    colonia = request.POST['barrio'], municipio = request.POST['municipio'], estado = request.POST['estado'],propietario = request.POST['propietario'],
    parentesco = request.POST['parentesco'])

    context = {
        'datosPersonalesModel': datosPersonalesModel,
    }
    return render(request,'temporal.html',context)
