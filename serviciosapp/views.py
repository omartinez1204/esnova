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
    ocupacion_tercero = request.POST['ocupacion_tercero'], responsable_misma_persona = request.POST['responsable_misma_persona'])
    datosdequienesDependes.save()
    context = {
        'datosdequienesDependes':datosdequienesDependes,
        'id_usuario_actual':id_usuario_actual,
    }
    #validadr formulario 5 o 6
    if (request.POST['responsable_misma_persona'] == 'Si'):
        return render(request,'ingreso_familiar.html', context)
    else :
        return render(request,'datos_responsable5.html', context)

#formulario 5
def obtenerDatos_Responsable(request):
    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
    datosresponsable = datosDelResponsable(usuario_foraneo = consulta_datosPersonales  ,ap_paterno = request.POST['apellido_paterno'], ap_materno = request.POST['apellido_materno'],
    nombre = request.POST['nombre'], sexo =  request.POST['sexo'], edad = int(request.POST['edad']), estado_civil = request.POST['estado_civil'],
    telefono_fijo = request.POST['telefono'], celular = request.POST['celular'], parentesco = request.POST['parentesco'], calle = request.POST['calle'],
    numero = int(request.POST['numero']), colonia = request.POST['colonia'], municipio = request.POST['municipio'], region = request.POST['region'],
    estado = request.POST['estado'], grado_escolaridad = request.POST['inlineRadioOptions_1'], tipo_de_trabajo = request.POST['tipo_de_trabajo'],
    ocupacion = request.POST['ocupacion'],texto_ocupacion = request.POST['texto_ocupacion'], empresa = request.POST['empresa'], cargo  = request.POST['cargo'],
    area = request.POST['area'], antiguedad = request.POST['antiguedad'], telefono_empresa = request.POST['telefono_empresa'], calle_empresa = request.POST['calle_empresa'],
    numero_empresa = request.POST['numero_empresa'], colonia_empresa = request.POST['colonia_empresa'], municipio_empresa = request.POST['municipio_empresa'],
    region_empresa = request.POST['region_empresa'], estado_empresa = request.POST['estado_empresa'])
    datosresponsable.save()
    context = {
        'datosresponsable':datosresponsable,
        'id_usuario_actual':id_usuario_actual,
    }

    return render(request,'ingreso_familiar.html', context)
#formulario 6
def obtenerIngresoFamiliar(request):
    v1 = False
    try:
        if  'Si' == request.POST['apoyo_F_E']:
            v1 = True
    except Exception as e:
        v1 = False

    try :
        ingreso_nombre_1 = float(request.POST['ingreso_nombre_1'])
    except ValueError:
        ingreso_nombre_1 = 0.0
    try :
        ingreso_nombre_2 = float(request.POST['ingreso_nombre_2'])
    except ValueError:
        ingreso_nombre_2 = 0.0

    #id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = 1)
    id_usuario_actual = 1;

    if request.POST['apoyo_F_E'] == 'Si':

        if request.POST['tipo_de_apoyo'] == 'Otro':
            numero_folio_ = ''
            monto_folio_ = 0
        else :
            otro_especifique_ = ''
            iniciativa_privada_ = ''
            monto_i_p_ = 0

        datosingresofamiliar = ingresoFamiliarMensual(usuario_foraneo =  consulta_datosPersonales, personas_que_trabajan = request.POST['personas_que_trabajan'], ingreso_padre = request.POST['ingreso_padre'],
        ingreso_madre = request.POST['ingreso_madre'], otro_nombre_1 = request.POST['otro_nombre_1'], otro_nombre_2 = request.POST['otro_nombre_2'],
        ingreso_nombre_1 = ingreso_nombre_1, ingreso_nombre_2 = ingreso_nombre_2, apoyo_F_E = v1, tipo_de_apoyo = request.POST['tipo_de_apoyo'],
        numero_folio = numero_folio_ , monto_folio = monto_folio_, otro_especifique = otro_especifique_,
        iniciativa_privada = iniciativa_privada_, monto_i_p = monto_i_p_, numero_persona_dep = request.POST['numero_persona_dep'],
        ingreso_mensual_total = request.POST['ingreso_mensual_total'])

    else:
        numero_folio_ = ''
        monto_folio_ = 0
        otro_especifique_ = ''
        iniciativa_privada_ = ''
        monto_i_p_ = 0
        datosingresofamiliar = ingresoFamiliarMensual(usuario_foraneo =  consulta_datosPersonales, personas_que_trabajan = request.POST['personas_que_trabajan'], ingreso_padre = request.POST['ingreso_padre'],
        ingreso_madre = request.POST['ingreso_madre'], otro_nombre_1 = request.POST['otro_nombre_1'], otro_nombre_2 = request.POST['otro_nombre_2'],
        ingreso_nombre_1 = ingreso_nombre_1, ingreso_nombre_2 = ingreso_nombre_2, apoyo_F_E = v1, tipo_de_apoyo = request.POST['tipo_de_apoyo'],
        numero_folio = numero_folio_ , monto_folio = monto_folio_, otro_especifique = otro_especifique_,
        iniciativa_privada = iniciativa_privada_, monto_i_p = monto_i_p_, numero_persona_dep = request.POST['numero_persona_dep'],
        ingreso_mensual_total = request.POST['ingreso_mensual_total'])

    datosingresofamiliar.save()
    context = {
        'datosingresofamiliar':datosingresofamiliar,
        'id_usuario_actual':id_usuario_actual,
    }
    return render(request,'gasto_familiar.html', context)
#formulario 7
def obtenerGastoFamiliar(request):

    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
    datosgastofamiliar = gastoFamiliarMensual(usuario_foraneo = consulta_datosPersonales, agua = request.POST['agua'], luz = request.POST['luz'], telefono = request.POST['telefono'],
    gas = request.POST['gas'], educacion = request.POST['educacion'], transporte = request.POST['transporte'], renta = request.POST['renta'], television_por_cable = request.POST['television_por_cable'],
    internet = request.POST['internet'], nombre_gasto_1 = request.POST['Otros_1_nombre'], otros_gastos_1 = request.POST['otros_1'], gasto_alimentacion = request.POST['gasto_alimentacion'], gastos_vestido = request.POST['gastos_vestido'],
    gastos_servicios_medicos = request.POST['gastos_servicios_medicos'], gasto_diversion = request.POST['gasto_diversion'], nombre_gasto_2 = request.POST['otros_gastos_1_nombre'], otros_gastos_2 = request.POST['otros_gastos_1'],
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

def obtenerInformacionAdicional(request):
    consulta_datosPersonales = Usuario.objects.get(pk = 1)

    v1 = False
    v2 = False
    v3 = False
    v4 = False
    v5 = False
    v6 = False
    v7 = False
    v8 = False
    v9 = False
    v10 = False
    try:
        if  'True' == request.POST['comedor']:
            v1 = True
    except Exception as e:
        v1 = False

    try:
        if  request.POST['sala'] == 'True':
            v2 = True
    except Exception as e:
        v2 = False
    try:
        if  request.POST['biblioteca'] == 'True':
            v3 = True
    except Exception as e:
        v3 = False

    try:
        if  request.POST['terraza'] == 'True':
            v4 = True
    except Exception as e:
        v4 = False

    try:
        if  request.POST['cuarto_estudio'] == 'True':
            v5 = True
    except Exception as e:
        v5 = False

    try:
        if  request.POST['patio'] == 'True':
            v6 = True
    except Exception as e:
        v6 = False
    try:
        if  request.POST['cochera'] == 'True':
            v7 = True
    except Exception as e:
        v7 = False

    try:
        if  request.POST['cuarto_servicio'] == 'True':
            v8 = True
    except Exception as e:
        v8 = False
    try:
        if  request.POST['automovil'] == 'True':
            v9 = True
    except Exception as e:
        v9 = False
    try:
        if  request.POST['apoyo_dependencia'] == 'True':
            v10 = True
    except Exception as e:
        v10 = False

    if v9 == True:
        if v10 == True:
            datosInformacionAdicional = informacionSocioEconomica(usuario_fore = consulta_datosPersonales, casa_familiar = request.POST['casa_familiar'], material_paredes = request.POST['material_paredes'], material_piso = request.POST['material_piso'],
            material_techo = request.POST['material_techo'], tipo_vivienda = request.POST['tipo_vivienda'], servicios_publicos = request.POST['servicios_publicos'], servicios_vivienda = request.POST['servicios_vivienda'],
            casa_cuenta_con = request.POST['casa_cuenta_con'], personas_habitan = request.POST['personas_habitan'], cuartos = request.POST['cuartos'], banios = request.POST['material_techo'], banios_tipo = request.POST['banios_tipo'],
            cocina_tipo = request.POST['cocina_tipo'], comedor = v1, sala = v2, biblioteca = v3, terraza = v4, cuarto_estudio = v5, patio = v6, cochera = v7, cuarto_servicio = v8, otro = request.POST['otro'], focos = request.POST['focos'],
            automovil = v9, marca = request.POST['marca'], modelo = request.POST['modelo'], anio = request.POST['anio'], tipo_cultivo = request.POST['tipo_cultivo'], otros_bienes = request.POST['otros_bienes'],
            negocio = request.POST['negocio'], tipo_negocio = request.POST['tipo_negocio'], otros_bienes_especifique = request.POST['otros_bienes_especifique'], servicios_asistencia_medica = request.POST['servicios_asistencia_medica'],
            otros_servicios = request.POST['otros_servicios'], apoyo_dependencia = v10, en_especie = request.POST['en_especie'], monto_apoyo = request.POST['monto_apoyo'], dependencia_empresa = request.POST['dependencia_empresa'],
            periodo_apoyo = request.POST['periodo_apoyo'])
        else:
            datosInformacionAdicional = informacionSocioEconomica(usuario_fore = consulta_datosPersonales, casa_familiar = request.POST['casa_familiar'], material_paredes = request.POST['material_paredes'], material_piso = request.POST['material_piso'],
            material_techo = request.POST['material_techo'], tipo_vivienda = request.POST['tipo_vivienda'], servicios_publicos = request.POST['servicios_publicos'], servicios_vivienda = request.POST['servicios_vivienda'],
            casa_cuenta_con = request.POST['casa_cuenta_con'], personas_habitan = request.POST['personas_habitan'], cuartos = request.POST['cuartos'], banios = request.POST['material_techo'], banios_tipo = request.POST['banios_tipo'],
            cocina_tipo = request.POST['cocina_tipo'], comedor = v1, sala = v2, biblioteca = v3, terraza = v4, cuarto_estudio = v5, patio = v6, cochera = v7, cuarto_servicio = v8, otro = request.POST['otro'], focos = request.POST['focos'],
            automovil = v9, marca = request.POST['marca'], modelo = request.POST['modelo'], anio = request.POST['anio'], tipo_cultivo = request.POST['tipo_cultivo'], otros_bienes = request.POST['otros_bienes'],
            negocio = request.POST['negocio'], tipo_negocio = request.POST['tipo_negocio'], otros_bienes_especifique = request.POST['otros_bienes_especifique'], servicios_asistencia_medica = request.POST['servicios_asistencia_medica'],
            otros_servicios = request.POST['otros_servicios'], apoyo_dependencia = v10)
    else:
        if v10 == True:
            datosInformacionAdicional = informacionSocioEconomica(usuario_fore = consulta_datosPersonales, casa_familiar = request.POST['casa_familiar'], material_paredes = request.POST['material_paredes'], material_piso = request.POST['material_piso'],
            material_techo = request.POST['material_techo'], tipo_vivienda = request.POST['tipo_vivienda'], servicios_publicos = request.POST['servicios_publicos'], servicios_vivienda = request.POST['servicios_vivienda'],
            casa_cuenta_con = request.POST['casa_cuenta_con'], personas_habitan = request.POST['personas_habitan'], cuartos = request.POST['cuartos'], banios = request.POST['material_techo'], banios_tipo = request.POST['banios_tipo'],
            cocina_tipo = request.POST['cocina_tipo'], comedor = v1, sala = v2, biblioteca = v3, terraza = v4, cuarto_estudio = v5, patio = v6, cochera = v7, cuarto_servicio = v8, otro = request.POST['otro'], focos = request.POST['focos'],
            automovil = v9, tipo_cultivo = request.POST['tipo_cultivo'], otros_bienes = request.POST['otros_bienes'],
            negocio = request.POST['negocio'], tipo_negocio = request.POST['tipo_negocio'], otros_bienes_especifique = request.POST['otros_bienes_especifique'], servicios_asistencia_medica = request.POST['servicios_asistencia_medica'],
            otros_servicios = request.POST['otros_servicios'], apoyo_dependencia = v10, en_especie = request.POST['en_especie'], monto_apoyo = request.POST['monto_apoyo'], dependencia_empresa = request.POST['dependencia_empresa'],
            periodo_apoyo = request.POST['periodo_apoyo'])
        else:
            datosInformacionAdicional = informacionSocioEconomica(usuario_fore = consulta_datosPersonales, casa_familiar = request.POST['casa_familiar'], material_paredes = request.POST['material_paredes'], material_piso = request.POST['material_piso'],
            material_techo = request.POST['material_techo'], tipo_vivienda = request.POST['tipo_vivienda'], servicios_publicos = request.POST['servicios_publicos'], servicios_vivienda = request.POST['servicios_vivienda'],
            casa_cuenta_con = request.POST['casa_cuenta_con'], personas_habitan = request.POST['personas_habitan'], cuartos = request.POST['cuartos'], banios = request.POST['material_techo'], banios_tipo = request.POST['banios_tipo'],
            cocina_tipo = request.POST['cocina_tipo'], comedor = v1, sala = v2, biblioteca = v3, terraza = v4, cuarto_estudio = v5, patio = v6, cochera = v7, cuarto_servicio = v8, otro = request.POST['otro'], focos = request.POST['focos'],
            automovil = v9, tipo_cultivo = request.POST['tipo_cultivo'], otros_bienes = request.POST['otros_bienes'],
            negocio = request.POST['negocio'], tipo_negocio = request.POST['tipo_negocio'], otros_bienes_especifique = request.POST['otros_bienes_especifique'], servicios_asistencia_medica = request.POST['servicios_asistencia_medica'],
            otros_servicios = request.POST['otros_servicios'], apoyo_dependencia = v10)

    datosInformacionAdicional.save()
    context = {
        'datosInformacionAdicional':datosInformacionAdicional,
    }
    return render(request,'temporal.html', context)


def archivos(request):
    if request.method == 'POST':
        form = UpArchivos(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            form = UpArchivos()
            return render(request,'serviciosapp/anexar_documentacion.html',{'form':form})
    else:
        form = UpArchivos()
    return render(request,'serviciosapp/anexar_documentacion.html',{'form':form})

def imagenes(request):
    print("solicitando todos los doxumentos")
    imagenes = subirArchivos.objects.all()
    context = {
        'imagenes':imagenes
    }
    return render(request,'serviciosapp/archivos.html',context)

def obtenerInformacionAdicional(request):
    consulta_datosPersonales = Usuario.objects.get(pk = 1)

    v1 = False
    v2 = False
    v3 = False
    v4 = False
    v5 = False
    v6 = False
    v7 = False
    v8 = False
    v9 = False
    v10 = False
    v11 = False
    v12 = False
    v13 = False
    v14 = False
    v15 = False
    v16 = False
    v17 = False
    v18 = False
    v19 = False
    v20 = False
    v21 = False
    v22 = False
    v23 = False
    v24 = False
    v25 = False
    v26 = False
    v27 = False
    v28 = False
    v29 = False
    v30 = False
    v31 = False
    v32 = False
    v33 = False

    try:
        if  'True' == request.POST['alumbrado_publico']:
            v1 = True
    except Exception as e:
        v1 = False
    try:
        if  request.POST['pavimentacion'] == 'True':
            v2 = True
    except Exception as e:
        v2 = False
    try:
        if  request.POST['drenaje_publico'] == 'True':
            v3 = True
    except Exception as e:
        v3 = False

    try:
        if  request.POST['telefono'] == 'True':
            v4 = True
    except Exception as e:
        v4 = False

    try:
        if  request.POST['television_por_cable'] == 'True':
            v5 = True
    except Exception as e:
        v5 = False

    try:
        if  request.POST['agua'] == 'True':
            v6 = True
    except Exception as e:
        v6 = False
    try:
        if  request.POST['luz'] == 'True':
            v7 = True
    except Exception as e:
        v7 = False

    try:
        if  request.POST['drenaje'] == 'True':
            v8 = True
    except Exception as e:
        v8 = False
    try:
        if  request.POST['calentador_de_gas'] == 'True':
            v9 = True
    except Exception as e:
        v9 = False
    try:
        if  'True' == request.POST['aire_acondicionado']:
            v10 = True
    except Exception as e:
        v10 = False
    try:
        if  request.POST['estufa_de_gas'] == 'True':
            v11 = True
    except Exception as e:
        v11 = False
    try:
        if  request.POST['lavadora'] == 'True':
            v12 = True
    except Exception as e:
        v12 = False

    try:
        if  request.POST['refrigerador'] == 'True':
            v13 = True
    except Exception as e:
        v13 = False

    try:
        if  request.POST['televisor'] == 'True':
            v14 = True
    except Exception as e:
        v14 = False

    try:
        if  request.POST['microondas'] == 'True':
            v15 = True
    except Exception as e:
        v15 = False
    try:
        if  request.POST['dvd'] == 'True':
            v16 = True
    except Exception as e:
        v16 = False

    try:
        if  request.POST['equipo_de_sonido'] == 'True':
            v17 = True
    except Exception as e:
        v17 = False
    try:
        if  request.POST['computadora_de_escritorio'] == 'True':
            v18 = True
    except Exception as e:
        v18 = False
    try:
        if  request.POST['aspiradora'] == 'True':
            v19 = True
    except Exception as e:
        v19 = False
    try:
        if  'True' == request.POST['videocamara']:
            v20 = True
    except Exception as e:
        v20 = False

    try:
        if  request.POST['podadora'] == 'True':
            v21 = True
    except Exception as e:
        v21 = False
    try:
        if  request.POST['laptop'] == 'True':
            v22 = True
    except Exception as e:
        v22 = False

    try:
        if  request.POST['videojuegos'] == 'True':
            v23 = True
    except Exception as e:
        v23 = False

    try:
        if  'True' == request.POST['comedor']:
            v24 = True
    except Exception as e:
        v24 = False

    try:
        if  request.POST['sala'] == 'True':
            v25 = True
    except Exception as e:
        v25 = False
    try:
        if  request.POST['biblioteca'] == 'True':
            v26 = True
    except Exception as e:
        v26 = False

    try:
        if  request.POST['terraza'] == 'True':
            v27 = True
    except Exception as e:
        v27 = False

    try:
        if  request.POST['cuarto_estudio'] == 'True':
            v28 = True
    except Exception as e:
        v28 = False

    try:
        if  request.POST['patio'] == 'True':
            v29 = True
    except Exception as e:
        v29 = False
    try:
        if  request.POST['cochera'] == 'True':
            v30 = True
    except Exception as e:
        v30 = False

    try:
        if  request.POST['cuarto_servicio'] == 'True':
            v31 = True
    except Exception as e:
        v31 = False
    try:
        if  request.POST['automovil'] == 'True':
            v32 = True
    except Exception as e:
        v32 = False
    try:
        if  request.POST['apoyo_dependencia'] == 'True':
            v33 = True
    except Exception as e:
        v33 = False
    try :
        anio_ = int(request.POST['anio'])
    except ValueError:
        anio_ = 0
    try :
        monto_apoyo_ = float(request.POST['monto_apoyo'])
    except ValueError:
        monto_apoyo_ = 0.0

    datosInformacionAdicional = informacionSocioEconomica(usuario_fore = consulta_datosPersonales, casa_familiar = request.POST['casa_familiar'], material_paredes = request.POST['material_paredes'], material_piso = request.POST['material_piso'],
    material_techo = request.POST['material_techo'], tipo_vivienda = request.POST['tipo_vivienda'], alumbrado_publico = v1, pavimientacion = v2, drenaje_publico = v3, otro_servicio = request.POST['otro_servicio'],
    telefono = v4, television_por_cable = v5, agua = v6, luz = v7, drenaje =v8, otro_servicio_vivienda = request.POST['otro_servicio_vivienda'], calentador_de_gas = v9, aire_acondicionado = v10, estufa_de_gas = v11, lavadora = v12, refrigerador = v13,
    televisor = v14, microondas = v15, dvd = v16, equipo_de_sonido = v17, computadora_de_escritorio = v18, aspiradora = v19, videocamara = v20, podadora = v21, laptop = v22, videojuegos = v23,
    personas_habitan = request.POST['personas_habitan'], cuartos = request.POST['cuartos'], banios = request.POST['material_techo'], banios_tipo = request.POST['banios_tipo'],
    cocina_tipo = request.POST['cocina_tipo'], comedor = v24, sala = v25, biblioteca = v26, terraza = v27, cuarto_estudio = v28, patio = v29, cochera = v30, cuarto_servicio = v31, otro = request.POST['otro'], focos = request.POST['focos'],
    automovil = v32, marca = request.POST['marca'], modelo = request.POST['modelo'], anio = anio_, tipo_cultivo = request.POST['tipo_cultivo'], otros_bienes = request.POST['otros_bienes'],
    negocio = request.POST['negocio'], tipo_negocio = request.POST['tipo_negocio'], otros_bienes_especifique = request.POST['otros_bienes_especifique'], servicios_asistencia_medica = request.POST['servicios_asistencia_medica'],
    otros_servicios = request.POST['otros_servicios'], apoyo_dependencia = v33, en_especie = request.POST['en_especie'], monto_apoyo = monto_apoyo_, dependencia_empresa = request.POST['dependencia_empresa'],
    periodo_apoyo = request.POST['periodo_apoyo'])

    datosInformacionAdicional.save()
    context = {
        'datosInformacionAdicional':datosInformacionAdicional,
    }
    return render(request,'temporal.html', context)
