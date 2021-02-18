from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *
from datetime import datetime,date
from serviciosapp.forms import *
from django.views import View
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.
id_usuario_actual = 0

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def obtenerDatos_Solicitante(request):
    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)

    obtener_usuario = 

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

#segundo formulario
def obtenerGastos_Solicitante(request):
    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
    v1 = True
    v2 = True
    v3 = True
    if not request.POST['gastos_adicionales']:
        gastos_adicionales_  = 0
    else:
        gastos_adicionales_ = request.POST["gastos_adicionales"]
    if not request.POST["cant_personas_renta"]:
        cant_personas_renta_ = 0
    else:
        cant_personas_renta_ = request.POST["cant_personas_renta"]
    if not request.POST["renta_mensual"]:
        renta_mensual_= 0
    else:
        renta_mensual_ = request.POST["renta_mensual"]
    if not request.POST["cant_familiares_renta"]:
        cant_familiares_renta_ = 0
    else:
        cant_familiares_renta_ = request.POST["cant_familiares_renta"]
    if not request.POST["parentesco_arrentador"]:
        parentesco_arrentador_ = ""
    else:
        parentesco_arrentador_ = request.POST["parentesco_arrentador"]
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

    if request.POST["trabaja"]:
        ingreso_mensual_ = 0

    if not request.POST["personas_dependientes"]:
        personas_dependientes_ = 0
    else:
        personas_dependientes_ = request.POST["personas_dependientes"]


    datosGastosSolicitante = gastosDelSolicitante(usuario_foraneo  = consulta_datosPersonales,gastos_mensuales = request.POST['gastos_mensuales'], gastos_adicionales = gastos_adicionales_,
    cant_personas_renta = cant_personas_renta_ , renta_mensual = renta_mensual_ , cant_familiares_renta = cant_familiares_renta_ ,
    parentesco_arrentador = parentesco_arrentador_ , medio_de_transporte = request.POST['medio_de_transporte'], datos_transporte_propio = request.POST['datos_transporte_propio'],
    celular = request.POST['celular'], celular_marca =request.POST['celular_marca'], celular_modelo = request.POST['celular_modelo'], camara_fotografica = v1, reproductor_de_audio = v2,
    tableta_electronica = v3, centro_de_trabajo = request.POST['centro_de_trabajo'], ingreso_mensual =  ingreso_mensual_ , datos_trabajo = request.POST['datos_trabajo'],
    jefe_de_familia = request.POST['jefe_de_familia'], personas_dependientes = personas_dependientes_)
    datosGastosSolicitante.save()

    context = {
        'datosGastosSolicitante':datosGastosSolicitante,
        'id_usuario_actual':id_usuario_actual,
    }
    return render(request,'medios_estudiar.html', context)

def obtenermedios_estudiar(request):

    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
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
    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
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
    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
    t_nombre = request.POST['t_nombre']
    t_edad = request.POST['t_edad']
    t_parentesco = request.POST['t_parentesco']
    t_comprobante = request.POST['t_comprobante']
    t_observaciones = request.POST['t_observaciones']
    atributo = ""
    lista_nombre = list()
    lista_edad = list()
    lista_parentesco = list()
    lista_comprobante = list()
    lista_observaciones = list()

    if t_nombre != "":
        for l in t_nombre:
            if l != '╣':
                atributo = atributo+l
            else:
                lista_nombre.append(atributo)
                atributo = ""
        for l in t_edad:
            if l != '╣':
                atributo = atributo+l
            else:
                lista_edad.append(int(atributo))
                atributo = ""
        for l in t_parentesco:
            if l != '╣':
                atributo = atributo+l
            else:
                lista_parentesco.append(atributo)
                atributo = ""
        for l in t_comprobante:
            if l != '╣':
                atributo = atributo+l
            else:
                lista_comprobante.append(atributo)
                atributo = ""
        for l in t_observaciones:
            if l != '╣':
                atributo = atributo+l
            else:
                lista_observaciones.append(atributo)
                atributo = ""

    datospersonasquedependen = personasQueDependenDelIngresoMensual(usuario_fore = consulta_datosPersonales, numero_hermanos = request.POST['num_hermanos'])
    datospersonasquedependen.save()
    for i in range(0, len(lista_nombre), 1):
        p = PersonaDependiente(nombre = lista_nombre[i], edad = lista_edad[i], parentesco = lista_parentesco[i],
        tipo_comprobante = lista_comprobante[i], observaciones = lista_observaciones[i])
        p.save()
        print(p)
        datospersonasquedependen.personas.add(p)

    context = {
        'datospersonasquedependen':datospersonasquedependen,
        'id_usuario_actual':id_usuario_actual,
    }
    return render(request,'informacion_adicional.html', context)

def obtenerInformacionAdicional(request):
    id_usuario_actual = int(request.POST['id_usuario'])
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)

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
        if  'True' == request.POST['alumbrado']:
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
    material_techo = request.POST['material_techo'], tipo_vivienda = request.POST['tipo_vivienda'], alumbrado_publico = v1, pavimentacion = v2, drenaje_publico = v3, otro_servicio = request.POST['otro_servicio'],
    telefono = v4, television_por_cable = v5, agua = v6, luz = v7, drenaje =v8, otro_servicio_vivienda = request.POST['otro_servicio_vivienda'], calentador_de_gas = v9, aire_acondicionado = v10, estufa_de_gas = v11, lavadora = v12, refrigerador = v13,
    televisor = v14, microondas = v15, dvd = v16, equipo_de_sonido = v17, computadora_de_escritorio = v18, aspiradora = v19, videocamara = v20, podadora = v21, laptop = v22, videojuegos = v23,
    personas_habitan = request.POST['personas_habitan'], cuartos = request.POST['cuartos'], banios = request.POST['banios'], banios_tipo = request.POST['banios_tipo'],
    cocina_tipo = request.POST['cocina_tipo'], comedor = v24, sala = v25, biblioteca = v26, terraza = v27, cuarto_estudio = v28, patio = v29, cochera = v30, cuarto_servicio = v31, otro = request.POST['otro'], focos = request.POST['focos'],
    automovil = v32, marca = request.POST['marca'], modelo = request.POST['modelo'], anio = anio_, tipo_cultivo = request.POST['tipo_cultivo'], otros_bienes = request.POST['otros_bienes'],
    negocio = request.POST['negocio'], tipo_negocio = request.POST['tipo_negocio'], otros_bienes_especifique = request.POST['otros_bienes_especifique'], servicios_asistencia_medica = request.POST['servicios_asistencia_medica'],
    apoyo_dependencia = v33, en_especie = request.POST['en_especie'], monto_apoyo = monto_apoyo_, dependencia_empresa = request.POST['dependencia_empresa'],
    periodo_apoyo = request.POST['periodo_apoyo'])

    datosInformacionAdicional.save()
    form = UpArchivos()
    form.usuario_fore = id_usuario_actual
    context = {
        'datosInformacionAdicional':datosInformacionAdicional,
        'id_usuario_actual':id_usuario_actual,
        'form':form,
    }
    return render(request,'anexar_documentacion.html', context)

def archivos(request):
    try:
        id_usuario_actual = int(request.POST['id_usuario'])
    except Exception as e:
        id_usuario_actual = 1
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)

    if request.method == 'POST':
        form = UpArchivos(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario_fore = consulta_datosPersonales
            instance.save()
            form = UpArchivos()
            context = {
                'id_usuario_actual':id_usuario_actual,
                'form':form,
            }
            return render(request,'anexar_documentacion.html',context)
    else:
        form = UpArchivos()
        context = {
            'id_usuario_actual':id_usuario_actual,
            'form':form,
        }
    return render(request,'anexar_documentacion.html',context)

def imagenes(request):
    try:
        id_usuario_actual = int(request.POST['id_usuario'])
    except Exception as e:
        id_usuario_actual = 1
    consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
    print("solicitando todos los documentos")
    imagenes = subirArchivos.objects.all().filter(usuario_fore = consulta_datosPersonales)

    context = {
        'imagenes':imagenes,
        'id_usuario_actual':id_usuario_actual,
    }
    return render(request,'archivos.html',context)


class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		id_usuario_actual = int(request.GET['id_usuario'])
		consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
		try:
			f1 = datosPersonales.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f1 = datosPersonales()
		try:
			f2 = gastosDelSolicitante.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f2 = gastosDelSolicitante()
		try:
			f3 = mediosParaEstudiar.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f3 = mediosParaEstudiar()
		try:
			f4 = datosPersonaDeQuienDepende.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f4 = datosPersonaDeQuienDepende()
		try:
			f5 = datosDelResponsable.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f5 = datosDelResponsable()
		try:
			f6 = ingresoFamiliarMensual.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f6 = ingresoFamiliarMensual()
		try:
			f7 = gastoFamiliarMensual.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f7 = gastoFamiliarMensual()
		try:
			f8 = PersonaDependiente.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f8 = PersonaDependiente()
		try:
			f9 = personasQueDependenDelIngresoMensual.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f9 = personasQueDependenDelIngresoMensual()

		data = {
				'id_usuario_actual':id_usuario_actual,
				'f1':f1,
				'f2':f2,
				'f3':f3,
				'f4':f4,
				'f5':f5,
				'f6':f6,
				'f7':f7,
				'f8':f8,
				'f9':f9,
			}
		pdf = render_to_pdf('plantilla_pdf.html', data)
		return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		id_usuario_actual = int(request.GET['id_usuario'])
		consulta_datosPersonales = Usuario.objects.get(pk = id_usuario_actual)
		try:
			f1 = datosPersonales.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f1 = datosPersonales()
		try:
			f2 = gastosDelSolicitante.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f2 = gastosDelSolicitante()
		try:
			f3 = mediosParaEstudiar.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f3 = mediosParaEstudiar()
		try:
			f4 = datosPersonaDeQuienDepende.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f4 = datosPersonaDeQuienDepende()
		try:
			f5 = datosDelResponsable.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f5 = datosDelResponsable()
		try:
			f6 = ingresoFamiliarMensual.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f6 = ingresoFamiliarMensual()
		try:
			f7 = gastoFamiliarMensual.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f7 = gastoFamiliarMensual()
		try:
			f8 = PersonaDependiente.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f8 = PersonaDependiente()
		try:
			f9 = personasQueDependenDelIngresoMensual.objects.get(pk = id_usuario_actual)
		except Exception as e:
			f9 = personasQueDependenDelIngresoMensual()

		data = {
				'id_usuario_actual':id_usuario_actual,
				'f1':f1,
				'f2':f2,
				'f3':f3,
				'f4':f4,
				'f5':f5,
				'f6':f6,
				'f7':f7,
				'f8':f8,
				'f9':f9,
			}
		pdf = render_to_pdf('plantilla_pdf.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response
