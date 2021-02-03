from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *
from datetime import datetime,date

# Create your views here.
id_usuario_actual = 0

def obtenerDatos_Solicitante(request):
    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)

    if request.POST['residencia_distinta'] == 'Si':
        datosPersonalesModel = datosPersonales(usuario_foraneo = consulta_datosPersonales,fecha = date.today(), solicita_beca_alimentaria= request.POST['solicita_beca_alimentaria'],
        ap_paterno=request.POST['apellido_paterno'], ap_materno = request.POST['apellido_materno'], nombre = request.POST['nombre'],
        sexo = request.POST['sexo'], edad = request.POST['edad'], estado_civil = request.POST['estado_civil'], carrera =request.POST['carrera'],
        semestre = request.POST['semestre'],grupo = request.POST['grupo'],telefono = request.POST['celular'], otro_idiona =  request.POST['otro_idioma'],
        residencia_distinta = request.POST['residencia_distinta'] , calle =  request.POST['calle'], numero = request.POST['numero_calle'],
        colonia = request.POST['barrio'], municipio = request.POST['municipio'], estado = request.POST['estado'],propietario = request.POST['propietario'],
        parentesco = request.POST['parentesco'])
    else :
        datosPersonalesModel = datosPersonales(usuario_foraneo = consulta_datosPersonales, fecha = date.today(), solicita_beca_alimentaria= request.POST['solicita_beca_alimentaria'],
        ap_paterno=request.POST['apellido_paterno'], ap_materno = request.POST['apellido_materno'], nombre = request.POST['nombre'],
        sexo = request.POST['sexo'], edad = request.POST['edad'], estado_civil = request.POST['estado_civil'], carrera =request.POST['carrera'],
        semestre = request.POST['semestre'],grupo = request.POST['grupo'],telefono = request.POST['celular'], otro_idiona =  request.POST['otro_idioma'],
        residencia_distinta = '' , calle =  '', numero = 0, colonia = '', municipio = '', estado ='',propietario = '', parentesco = '')

    datosPersonalesModel.save()
    context = {
        'datosPersonalesModel': datosPersonalesModel,
        'id_usuario_actual': id_usuario_actual,
    }
    return render(request,'Gastos_Solicitante.html',context)

def obtenerGastos_Solicitante(request):
    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = 1)

    v1 = True
    v2 = True
    v3 = True
    try:
        if  1 == request.POST['camara_fotografica']:
            v1 = True
    except Exception as e:
        v1 = False

    try:
        if  1 == request.POST['reproductor_de_audio']:
            v2 = True
    except Exception as e:
        v2 = False

    try:
        if  1 == request.POST['tableta_electronica']:
            v3 = True
    except Exception as e:
        v3 = False

    if request.POST['celular'] == 'Si':
        if request.POST['jefe_de_familia'] == 'Si':
            datosGastosSolicitante = gastosDelSolicitante(usuario_foraneo  = consulta_datosPersonales,gastos_mensuales = request.POST['gastos_mensuales'], gastos_adicionales = request.POST['gastos_adicionales'],
            cant_personas_renta = request.POST['cant_personas_renta'], renta_mensual = request.POST['renta_mensual'], cant_familiares_renta = request.POST['cant_familiares_renta'],
            parentesco_arrentador = request.POST['parentesco_arrentador'], medio_de_transporte = request.POST['medio_de_transporte'], datos_transporte_propio = request.POST['datos_transporte_propio'],
            celular = request.POST['celular'], celular_marca = request.POST['celular_marca'], celular_modelo = request.POST['celular_modelo'], camara_fotografica = v1, reproductor_de_audio = v2,
            tableta_electronica = v3, centro_de_trabajo = request.POST['centro_de_trabajo'], ingreso_mensual = request.POST['ingreso_mensual'], datos_trabajo = request.POST['datos_trabajo'],
            jefe_de_familia = request.POST['jefe_de_familia'], personas_dependientes = request.POST['personas_dependientes'])
        else:
            datosGastosSolicitante = gastosDelSolicitante(usuario_foraneo  = consulta_datosPersonales,gastos_mensuales = request.POST['gastos_mensuales'], gastos_adicionales = request.POST['gastos_adicionales'],
            cant_personas_renta = request.POST['cant_personas_renta'], renta_mensual = request.POST['renta_mensual'], cant_familiares_renta = request.POST['cant_familiares_renta'],
            parentesco_arrentador = request.POST['parentesco_arrentador'], medio_de_transporte = request.POST['medio_de_transporte'], datos_transporte_propio = request.POST['datos_transporte_propio'],
            celular = request.POST['celular'], celular_marca = request.POST['celular_marca'], celular_modelo = request.POST['celular_modelo'], camara_fotografica = v1, reproductor_de_audio = v2,
            tableta_electronica = v3, centro_de_trabajo = request.POST['centro_de_trabajo'], ingreso_mensual = request.POST['ingreso_mensual'], datos_trabajo = request.POST['datos_trabajo'],
            jefe_de_familia = request.POST['jefe_de_familia'])
    else:
        if request.POST['jefe_de_familia'] == 'Si':
            datosGastosSolicitante = gastosDelSolicitante(usuario_foraneo  = consulta_datosPersonales,gastos_mensuales = request.POST['gastos_mensuales'], gastos_adicionales = request.POST['gastos_adicionales'],
            cant_personas_renta = request.POST['cant_personas_renta'], renta_mensual = request.POST['renta_mensual'], cant_familiares_renta = request.POST['cant_familiares_renta'],
            parentesco_arrentador = request.POST['parentesco_arrentador'], medio_de_transporte = request.POST['medio_de_transporte'], datos_transporte_propio = request.POST['datos_transporte_propio'],
            celular = request.POST['celular'], camara_fotografica = v1, reproductor_de_audio = v2,
            tableta_electronica = v3, centro_de_trabajo = request.POST['centro_de_trabajo'], ingreso_mensual = request.POST['ingreso_mensual'], datos_trabajo = request.POST['datos_trabajo'],
            jefe_de_familia = request.POST['jefe_de_familia'], personas_dependientes = request.POST['personas_dependientes'])
        else:
            datosGastosSolicitante = gastosDelSolicitante(usuario_foraneo  = consulta_datosPersonales,gastos_mensuales = request.POST['gastos_mensuales'], gastos_adicionales = request.POST['gastos_adicionales'],
            cant_personas_renta = request.POST['cant_personas_renta'], renta_mensual = request.POST['renta_mensual'], cant_familiares_renta = request.POST['cant_familiares_renta'],
            parentesco_arrentador = request.POST['parentesco_arrentador'], medio_de_transporte = request.POST['medio_de_transporte'], datos_transporte_propio = request.POST['datos_transporte_propio'],
            celular = request.POST['celular'], camara_fotografica = v1, reproductor_de_audio = v2,
            tableta_electronica = v3, centro_de_trabajo = request.POST['centro_de_trabajo'], ingreso_mensual = request.POST['ingreso_mensual'], datos_trabajo = request.POST['datos_trabajo'],
            jefe_de_familia = request.POST['jefe_de_familia'])

    datosGastosSolicitante.save()

    context = {
        'datosGastosSolicitante':datosGastosSolicitante,
        'id_usuario_actual':id_usuario_actual,
    }

    return render(request,'medios_estudiar.html', context)

def obtenermedios_estudiar(request):

    id_usuario_actual = int(request.POST['id_usuario'])
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

    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
    datosmediosEstudiar = mediosParaEstudiar( usuario_foraneo = consulta_datosPersonales,computadora_de_escritorio = v1, laptop = v2,
    impresora = v3, dvd = v4, maquina_de_escribir =v5, calculadora =v6,
    escritorio =v7, enciclopedia =v8, libros_especializados = v9,
    telefonia =v10, banda_ancha = v11, falta_algun_medio= request.POST['falta_algun_medio'])
    datosmediosEstudiar.save()
    context = {
        'datosmediosEstudiar':datosmediosEstudiar,
        'id_usuario_actual': id_usuario_actual,
    }

    return render(request,'dependencias.html', context)

#formulario numero 4
def datosdelasPersonasQueDependes(request):

    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)

    datosdequienesDependes = datosPersonaDeQuienDepende( usuario_foraneo= consulta_datosPersonales, ap_paterno = request.POST['apellido_paterno'], ap_materno = request.POST['apellido_materno'],
    nombre = request.POST['nombre'], sexo =  request.POST['sexo'], edad = int(request.POST['edad']), estado_civil = request.POST['estado_civil'],
    telefono_fijo = request.POST['telefono'], celular = request.POST['celular'], parentesco = request.POST['parentesco'], calle = request.POST['calle'],
    numero = int(request.POST['numero']), colonia = request.POST['colonia'], municipio = request.POST['municipio'], region = request.POST['region'],
    estado = request.POST['estado'], grado_escolaridad = request.POST['inlineRadioOptions_1'], tipo_de_trabajo = request.POST['tipo_de_trabajo'],
    ocupacion = request.POST['ocupacion'], texto_ocupacion = request.POST['texto_ocupacion'], empresa = request.POST['empresa'], cargo  = request.POST['cargo'],
    area = request.POST['area'], antiguedad = request.POST['antiguedad'], telefono_empresa = request.POST['telefono_empresa'], calle_empresa = request.POST['calle_empresa'],
    numero_empresa = request.POST['numero_empresa'], colonia_empresa = request.POST['colonia_empresa'], municipio_empresa = request.POST['municipio_empresa'],
    region_empresa = request.POST['region_empresa'], estado_empresa = request.POST['estado_empresa'], ap_paterno_tercero = request.POST['ap_paterno_tercero'],
    ap_materno_tercero = request.POST['ap_materno_tercero'], nombre_tercero = request.POST['nombre_tercero'], edad_tercero = int(request.POST['edad_tercero']),
    parentesco_tercero = request.POST['parentesco_tercero'],telefono_tercero = request.POST['telefono_tercero'], celular_tercero = request.POST['celular_tercero'],
    ocupacion_tercero = request.POST['ocupacion_tercero'])
    datosdequienesDependes.save()
    context = {
        'datosdequienesDependes':datosdequienesDependes,
        'id_usuario_actual':id_usuario_actual,
    }

    return render(request,'datos_responsable5.html', context)

def obtenerDatos_Responsable(request):

    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
    datosresponsable = datosDelResponsable(usuario_foraneo = consulta_datosPersonales  ,ap_paterno = request.POST['apellido_paterno'], ap_materno = request.POST['apellido_materno'],
    nombre = request.POST['nombre'], sexo =  request.POST['sexo'], edad = int(request.POST['edad']), estado_civil = request.POST['estado_civil'],
    telefono_fijo = request.POST['telefono'], celular = request.POST['celular'], parentesco = request.POST['parentesco'], calle = request.POST['calle'],
    numero = int(request.POST['numero']), colonia = request.POST['colonia'], municipio = request.POST['municipio'], region = request.POST['region'],
    estado = request.POST['estado'], grado_escolaridad = request.POST['inlineRadioOptions_1'], tipo_de_trabajo = request.POST['tipo_de_trabajo'],
    ocupacion = request.POST['ocupacion'], empresa = request.POST['empresa'], cargo  = request.POST['cargo'],
    area = request.POST['area'], antiguedad = request.POST['antiguedad'], telefono_empresa = request.POST['telefono_empresa'], calle_empresa = request.POST['calle_empresa'],
    numero_empresa = request.POST['numero_empresa'], colonia_empresa = request.POST['colonia_empresa'], municipio_empresa = request.POST['municipio_empresa'],
    region_empresa = request.POST['region_empresa'], estado_empresa = request.POST['estado_empresa'])
    datosresponsable.save()
    context = {
        'datosresponsable':datosresponsable,
        'id_usuario_actual':id_usuario_actual,
    }

    return render(request,'ingreso_familiar.html', context)

def obtenerIngresoFamiliar(request):
    try:
        if  'Si' == request.POST['apoyo_F_E']:
            v1 = True
    except Exception as e:
        v1 = False

    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
    if request.POST['apoyo_F_E'] == 'Si':
        datosingresofamiliar = ingresoFamiliarMensual(usuario_foraneo =  consulta_datosPersonales, personas_que_trabajan = request.POST['personas_que_trabajan'], ingreso_padre = request.POST['ingreso_padre'],
        ingreso_madre = request.POST['ingreso_madre'], otro_nombre_1 = request.POST['otro_nombre_1'], otro_nombre_2 = request.POST['otro_nombre_2'],
        ingreso_nombre_1 = request.POST['ingreso_nombre_1'], ingreso_nombre_2 = request.POST['ingreso_nombre_2'], apoyo_F_E = v1, tipo_de_apoyo = request.POST['tipo_de_apoyo'],
        numero_folio = request.POST['numero_folio'], monto_folio = request.POST['monto_folio'], otro_especifique = request.POST['otro_especifique'],
        iniciativa_privada = request.POST['iniciativa_privada'], monto_i_p = request.POST['monto_i_p'], numero_persona_dep = request.POST['numero_persona_dep'],
        ingreso_mensual_total = request.POST['ingreso_mensual_total'])
    else:
        datosingresofamiliar = ingresoFamiliarMensual(usuario_foraneo =  consulta_datosPersonales, personas_que_trabajan = request.POST['personas_que_trabajan'], ingreso_padre = request.POST['ingreso_padre'],
        ingreso_madre = request.POST['ingreso_madre'], otro_nombre_1 = request.POST['otro_nombre_1'], otro_nombre_2 = request.POST['otro_nombre_2'],
        ingreso_nombre_1 = request.POST['ingreso_nombre_1'], ingreso_nombre_2 = request.POST['ingreso_nombre_2'], apoyo_F_E = v1,
        iniciativa_privada = request.POST['iniciativa_privada'], monto_i_p = request.POST['monto_i_p'], numero_persona_dep = request.POST['numero_persona_dep'],
        ingreso_mensual_total = request.POST['ingreso_mensual_total'])

    datosingresofamiliar.save()
    context = {
        'datosingresofamiliar':datosingresofamiliar,
        'id_usuario_actual':id_usuario_actual,
    }
    return render(request,'gasto_familiar.html', context)

def obtenerGastoFamiliar(request):

    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
    datosgastofamiliar = gastoFamiliarMensual(usuario_fore = consulta_datosPersonales, agua = request.POST['agua'], luz = request.POST['luz'], telefono = request.POST['telefono'],
    gas = request.POST['gas'], educacion = request.POST['educacion'], transporte = request.POST['transporte'], renta = request.POST['renta'], television_por_cable = request.POST['television_por_cable'],
    internet = request.POST['internet'], otros_1 = request.POST['otros_1'], otros_2 = request.POST['otros_2'], gasto_alimentacion = request.POST['gasto_alimentacion'], gastos_vestido = request.POST['gastos_vestido'],
    gastos_servicios_medicos = request.POST['gastos_servicios_medicos'], gasto_diversion = request.POST['gasto_diversion'], otros_gastos_1 = request.POST['otros_gastos_1'], otros_gastos_2 = request.POST['otros_gastos_2'],
    total_gastos = request.POST['total_gastos'])

    datosgastofamiliar.save()
    context = {
        'datosgastofamiliar':datosgastofamiliar,
        'id_usuario_actual':id_usuario_actual,
    }
    return render(request,'datos_personas_dependo.html', context)

def obtenerPersonasQueDependen(request):
    consulta_datosPersonales = Usuario.objects.get(pk = 1)

    datospersonasquedependen = personasQueDependenDelIngresoMensual(usuario_fore = consulta_datosPersonales, numero_hermanos = request.POST['numero_hermanos'],
    nombres_personas = request.POST['nombres_personas'], edades_personas = request.POST['edades_personas'], parentescos_personas = request.POST['parentescos_personas'], tipo_comprobante_personas = request.POST['tipo_comprobante_personas'],
    observaciones = request.POST['observaciones'])

    datospersonasquedependen.save()
    context = {
        'datospersonasquedependen':datospersonasquedependen,
    }
    return render(request,'temporal.html', context)
