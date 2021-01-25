from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *
from datetime import datetime,date

# Create your views here.

def obtenerDatos_Solicitante(request):

    #consulta_datosPersonales = datosPersonales.objects.get()

    datosPersonalesModel = datosPersonales(fecha = date.today(), solicita_beca_alimentaria= request.POST['solicita_beca_alimentaria'],
    ap_paterno=request.POST['apellido_paterno'], ap_materno = request.POST['apellido_materno'], nombre = request.POST['nombre'],
    sexo = request.POST['sexo'], edad = request.POST['edad'], estado_civil = request.POST['estado_civil'], carrera =request.POST['carrera'],
    semestre = request.POST['semestre'],grupo = request.POST['grupo'],telefono = request.POST['celular'], otro_idiona =  request.POST['otro_idioma'],
    residencia_distinta = request.POST['residencia_distinta'] , calle =  request.POST['calle'], numero = request.POST['numero_calle'],
    colonia = request.POST['barrio'], municipio = request.POST['municipio'], estado = request.POST['estado'],propietario = request.POST['propietario'],
    parentesco = request.POST['parentesco'])
    datosPersonalesModel.save()
    context = {
        'datosPersonalesModel': datosPersonalesModel,
    }
    return render(request,'temporal.html',context)


def obtenerGastos_Solicitante(request):
    return render(request,'temporal')
