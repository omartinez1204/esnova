from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *
from datetime import datetime,date

# Create your views here.

def obtenerDatos_Solicitante(request):

    #consulta_datosPersonales = datosPersonales.objects.get()
    if request.POST['residencia_distinta'] == 'Si':
        datosPersonalesModel = datosPersonales(fecha = date.today(), solicita_beca_alimentaria= request.POST['solicita_beca_alimentaria'],
        ap_paterno=request.POST['apellido_paterno'], ap_materno = request.POST['apellido_materno'], nombre = request.POST['nombre'],
        sexo = request.POST['sexo'], edad = request.POST['edad'], estado_civil = request.POST['estado_civil'], carrera =request.POST['carrera'],
        semestre = request.POST['semestre'],grupo = request.POST['grupo'],telefono = request.POST['celular'], otro_idiona =  request.POST['otro_idioma'],
        residencia_distinta = request.POST['residencia_distinta'] , calle =  request.POST['calle'], numero = request.POST['numero_calle'],
        colonia = request.POST['barrio'], municipio = request.POST['municipio'], estado = request.POST['estado'],propietario = request.POST['propietario'],
        parentesco = request.POST['parentesco'])
    else :
        datosPersonalesModel = datosPersonales(fecha = date.today(), solicita_beca_alimentaria= request.POST['solicita_beca_alimentaria'],
        ap_paterno=request.POST['apellido_paterno'], ap_materno = request.POST['apellido_materno'], nombre = request.POST['nombre'],
        sexo = request.POST['sexo'], edad = request.POST['edad'], estado_civil = request.POST['estado_civil'], carrera =request.POST['carrera'],
        semestre = request.POST['semestre'],grupo = request.POST['grupo'],telefono = request.POST['celular'], otro_idiona =  request.POST['otro_idioma'],
        residencia_distinta = '' , calle =  '', numero = 0, colonia = '', municipio = '', estado ='',propietario = '', parentesco = '')

    datosPersonalesModel.save()
    context = {
        'datosPersonalesModel': datosPersonalesModel,
    }
    return render(request,'temporal.html',context)


def obtenerGastos_Solicitante(request):
    return render(request,'temporal.html')

def obtenermedios_estudiar(request):

    try:
        if  'True' == request.POST['computadora_de_escritorio']:
            v1 = True
    except Exception as e:
        v1 = False

    try:
        if  request.POST['laptop'] == 'True':
            v2 = True
    except Exception as e:
        v2 = False
    try:
        if  request.POST['impresora'] == 'True':
            v3 = True
    except Exception as e:
        v3 = False

    try:
        if  request.POST['dvd'] == 'True':
            v4 = True
    except Exception as e:
        v4 = False

    try:
        if  request.POST['maquina_de_escribir'] == 'True':
            v5 = True
    except Exception as e:
        v5 = False

    try:
        if  request.POST['calculadora'] == 'True':
            v6 = True
    except Exception as e:
        v6 = False
    try:
        if  request.POST['escritorio'] == 'True':
            v7 = True
    except Exception as e:
        v7 = False

    try:
        if  request.POST['enciclopedia'] == 'True':
            v8 = True
    except Exception as e:
        v8 = False

    try:
        if  request.POST['libros_especializados'] == 'True':
            v9 = True
    except Exception as e:
        v9 = False
    try:
        if  request.POST['telefonia'] == 'True':
            v10 = True
    except Exception as e:
        v10 = False
    try:
        if  request.POST['banda_ancha'] == 'True':
            v11 = True
    except Exception as e:
        v11 = False


    datosmediosEstudiar = mediosParaEstudiar(computadora_de_escritorio = v1, laptop = v2,
    impresora = v3, dvd = v4, maquina_de_escribir =v5, calculadora =v6,
    escritorio =v7, enciclopedia =v8, libros_especializados = v9,
    telefonia =v10, banda_ancha = v11, falta_algun_medio= request.POST['falta_algun_medio'])
    datosmediosEstudiar.save()
    context = {
        'datosmediosEstudiar':datosmediosEstudiar,
    }

    return render(request,'temporal.html', context)

def datosdelasPersonasQueDependes(request):

    datosdequienesDependes = datosPersonaDeQuienDepende(ap_paterno = request.POST['apellido_paterno'], ar_materno = request.POST['apellido_materno'],
    nombre = request.POST['nombre'], sexo = request.POST['sexo_'], edad = int(request.POST['edad']), estado_civil = request.POST['estado_civil'],
    telefono_fijo = request.POST['telefono'], celular = request.POST['celular'], parentesco = request.POST['parentesco'], calle = request.POST['calle'],
    numero = request.POST['numero'], colonia = request.POST['colonia'], municipio = request.POST['municipio'], region = request.POST['region'],
    estado = request.POST['estado'], grado_escolaridad = request.POST['inlineRadioOptions_1'], tipo_de_trabajo = request.POST['tipo_de_trabajo'],
    ocupacion = request.POST['ocupacion'], texto_ocupacion = request.POST['texto_ocupacion'], empresa = request.POST['empresa'] cargo  = request.POST['cargo'],
    area = request.POST['area'], antiguedad = request.POST['antiguedad'], telefono_empresa = request.POST['telefono_empresa'], calle_empresa = request.POST['calle_empresa'],
    numero_empresa = request.POST['numero_empresa'], colonia_empresa = request.POST['colonia_empresa'], municipio_empresa = request.POST['municipio_empresa'],
    region_empresa = request.POST['region_empresa'], estado_empresa = request.POST['estado_empresa'], ap_paterno_tercero = request.POST['ap_paterno_tercero'],
    ap_materno_tercero = request.POST['ap_materno_tercero'], nombre_tercero = request.POST['nombre_tercero'], edad_tercero = request.POST['edad_tercero'],
    parentesco_tercero = request.POST['parentesco_tercero'],telefono_tercero = request.POST['telefono_tercero'], celular_tercero = request.POST['celular_tercero'],
    ocupacion_tercero = request.POST['ocupacion_tercero'])
    datosdequienesDependes.save()
    context = {
        'datosdequienesDependes':datosdequienesDependes,
    }

    return render(request,'temporal.html', context)
