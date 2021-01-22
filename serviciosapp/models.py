from django.db import models


#modelo usuarios
class usuarios(models.Model):
    matricula = models.CharField(max_length =30 )
    contrasenia = models.CharField(max_length = 30)
    email = models.EmailField()
    def __str__(self):
        return '{0}{1}{2}'.format(self.matricula, self.contrasenia, self.email)
    

# Create your models here.
class datosPersonales(models.Model):
    fecha = models.DateTimeField('fecha')
    solicita_beca_alimentaria = models.BooleanField()
    ap_paterno = models.CharField(max_length = 30)
    ap_materno = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    sexo = models.CharField(max_length = 3)
    edad = models.IntegerField(default=0)
    estado_civil = models.CharField(max_length = 30)
    carrera = models.CharField(max_length = 30)
    semestre = models.IntegerField(default=0)
    grupo = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 30)
    otro_idiona = models.CharField(max_length = 30)
    residencia_distinta = models.BooleanField()
    calle = models.CharField(max_length = 30)
    numero = models.IntegerField(default=0)
    colonia = models.CharField(max_length = 30)
    municipio = models.CharField(max_length = 30)
    estado = models.CharField(max_length = 30)
    propietario = models.CharField(max_length = 30)
    parentesco = models.CharField(max_length = 30)
    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}{16}{17}{18}{19}{20}'.format(self.fecha, self.solicita_beca_alimentaria,
        self.ap_paterno, self.ap_materno, self.nombre, self.sexo, self.edad, self.estado_civil, self.carrera, self.semestre, self.grupo,
        self.telefono, self.otro_idiona, self.residencia_distinta, self.calle, self.numero, self.colonia, self.municipio, self.estado,
        self.propietario, self.parentesco)

class gastosDelSolicitante(models.Model):
    gastos_mensuales = models.FloatField()
    gastos_adicionales = models.FloatField()
    cant_personas_renta = models.IntegerField(default=0)
    renta_mensual = models.FloatField()
    cant_familiares_renta = models.IntegerField(default=0)
    parentesco_arrentador = models.CharField(max_length = 30)
    medio_de_transporte = models.CharField(max_length = 30)
    datos_transporte_propio = models.CharField(max_length = 30)
    celular = models.BooleanField()
    celular_marca = models.CharField(max_length = 30)
    celular_modelo = models.CharField(max_length = 30)
    camara_fotografica = models.BooleanField()
    reproductor_de_audio = models.BooleanField()
    tableta_electronica = models.BooleanField()
    centro_de_trabajo = models.CharField(max_length = 30)
    ingreso_mensual = models.FloatField()
    datos_trabajo = models.CharField(max_length = 30)
    jefe_de_familia = models.BooleanField()
    personas_dependientes = models.IntegerField(default=0)
    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}{16}{17}{18}{19}'.format(self.gastos_mensuales, self.gastos_adicionales,
        self.cant_personas_renta, self.renta_mensual, self.cant_familiares_renta, self.parentesco_arrentador, self.medio_de_transporte,
        self.datos_transporte_propio, self.celular, self.celular_marca, self.celular_modelo,self.camara_fotografica, self.reproductor_de_audio,
        self.tableta_electronica, self.centro_de_trabajo, self.ingreso_mensual, self.datos_trabajo, self.jefe_de_familia, self.personas_dependientes)

class mediosParaEstudiar(models.Model):
    computadora_de_escritorio = models.BooleanField()
    laptop = models.BooleanField()
    impresora = models.BooleanField()
    dvd = models.BooleanField()
    maquina_de_escribir = models.BooleanField()
    calculadora = models.BooleanField()
    escritorio = models.BooleanField()
    enciclopedia = models.BooleanField()
    libros_especializados = models.BooleanField()
    telefonia = models.BooleanField()
    banda_ancha = models.BooleanField()
    falta_algun_medio = models.CharField(max_length = 30)
    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}'.format(self.computadora_de_escritorio, self.laptop,
        self.impresora, self.dvd, self.maquina_de_escribir, self.calculadora, self.escritorio, self.enciclopedia,
        self.libros_especializados, self.telefonia, self.banda_ancha, self.falta_algun_medio)

class datosPersonaDeQuienDepende(models.Model):
    ap_paterno = models.CharField(max_length = 30)
    ap_materno = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    sexo = models.CharField(max_length = 3)
    edad = models.IntegerField(default=0)
    estado_civil = models.CharField(max_length = 30)
    telefono_fijo = models.CharField(max_length = 30)
    celular = models.CharField(max_length = 30)
    parentesco = models.CharField(max_length = 30)
    calle = models.CharField(max_length = 30)
    numero = models.IntegerField(default=0)
    colonia = models.CharField(max_length = 30)
    municipio = models.CharField(max_length = 30)
    region = models.CharField(max_length = 30)
    estado = models.CharField(max_length = 30)
    grado_escolaridad = models.CharField(max_length = 30)
    tipo_de_trabajo = models.CharField(max_length = 30)
    ocupacion = models.CharField(max_length = 30)
    labores_del_campo = models.CharField(max_length = 30)
    negocio_propio = models.BooleanField()
    tipo_de_producto = models.CharField(max_length = 30)
    jubilado = models.BooleanField()
    dependencia_jubilo = models.CharField(max_length = 30)
    empresa = models.CharField(max_length = 30)
    cargo = models.CharField(max_length = 30)
    area = models.CharField(max_length = 30)
    antiguedad = models.CharField(max_length = 30)
    telefono_empresa = models.CharField(max_length = 30)
    calle_empresa = models.CharField(max_length = 30)
    numero_empresa = models.CharField(max_length = 30)
    colonia_empresa = models.CharField(max_length = 30)
    municipio_empresa = models.CharField(max_length = 30)
    region_empresa = models.CharField(max_length = 30)
    estado_empresa = models.CharField(max_length = 30)
    ap_paterno_tercero = models.CharField(max_length = 30)
    ap_materno_tercero = models.CharField(max_length = 30)
    nombre_tercero = models.CharField(max_length = 30)
    edad_tercero = models.IntegerField(default=0)
    parentesco_tercero = models.CharField(max_length = 30)
    telefono_tercero = models.CharField(max_length = 30)
    celular_tercero = models.CharField(max_length = 30)
    ocupacion_tercero = models.CharField(max_length = 30)
    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}{16}{17}{18}{19}{20}{21}{22}{23}{24}{25}{26}{27}{28}{29}{30}{31}{32}{33}{34}{35}{36}{37}{38}{39}{40}{41}}'.format(self.ap_paterno, self.ap_materno, self.nombre, self.sexo, self.edad, self.estado_civil, self.telefono_fijo, self.celular, self.parentesco,
        self.calle, self.numero, self.colonia, self.municipio, self.region, self.estado, self.grado_escolaridad, self.tipo_de_trabajo, self.ocupacion,
        self.labores_del_campo, self.negocio_propio, self.tipo_de_producto, self.jubilado, self.dependencia_jubilo, self.empresa, self.cargo,
        self.area, self.antiguedad, self.telefono_empresa, self.calle_empresa, self.numero_empresa, self.colonia_empresa, self.municipio_empresa,
        self.region_empresa, self.estado_empresa, self.ap_paterno_tercero, self.ap_materno_tercero, self.nombre_tercero, self.edad_tercero,
        self.parentesco_tercero, self.telefono_tercero, self.celular_tercero, self.ocupacion_tercero)


class datosDelResponsable(models.Model):
    ap_paterno = models.CharField(max_length = 30)
    ap_materno = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    sexo = models.CharField(max_length = 3)
    edad = models.IntegerField(default=0)
    estado_civil = models.CharField(max_length = 30)
    telefono_fijo = models.CharField(max_length = 30)
    celular = models.CharField(max_length = 30)
    parentesco = models.CharField(max_length = 30)
    calle = models.CharField(max_length = 30)
    numero = models.IntegerField(default=0)
    colonia = models.CharField(max_length = 30)
    municipio = models.CharField(max_length = 30)
    region = models.CharField(max_length = 30)
    estado = models.CharField(max_length = 30)
    grado_escolaridad = models.CharField(max_length = 30)
    tipo_de_trabajo = models.CharField(max_length = 30)
    ocupacion = models.CharField(max_length = 30)
    labores_del_campo = models.CharField(max_length = 30)
    negocio_propio = models.BooleanField()
    tipo_de_producto = models.CharField(max_length = 30)
    jubilado = models.BooleanField()
    dependencia_jubilo = models.CharField(max_length = 30)
    empresa = models.CharField(max_length = 30)
    cargo = models.CharField(max_length = 30)
    area = models.CharField(max_length = 30)
    antiguedad = models.CharField(max_length = 30)
    telefono_empresa = models.CharField(max_length = 30)
    calle_empresa = models.CharField(max_length = 30)
    numero_empresa = models.CharField(max_length = 30)
    colonia_empresa = models.CharField(max_length = 30)
    municipio_empresa = models.CharField(max_length = 30)
    region_empresa = models.CharField(max_length = 30)
    estado_empresa = models.CharField(max_length = 30)
    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}{16}{17}{18}{19}{20}{21}{22}{23}{24}{25}{26}{27}{28}{29}{30}{31}{32}{33}{34}{35}{36}{37}{38}{39}{40}{41}}'.format(self.ap_paterno, self.ap_materno, self.nombre, self.sexo, self.edad, self.estado_civil, self.telefono_fijo, self.celular, self.parentesco,
        self.calle, self.numero, self.colonia, self.municipio, self.region, self.estado, self.grado_escolaridad, self.tipo_de_trabajo, self.ocupacion,
        self.labores_del_campo, self.negocio_propio, self.tipo_de_producto, self.jubilado, self.dependencia_jubilo, self.empresa, self.cargo,
        self.area, self.antiguedad, self.telefono_empresa, self.calle_empresa, self.numero_empresa, self.colonia_empresa, self.municipio_empresa,
        self.region_empresa, self.estado_empresa)



class ingresoFamiliarMensual(models.Model):
    personas_que_trabajan = models.IntegerField(default=0)
    ingreso_padre =  models.FloatField()
    ingreso_madre =  models.FloatField()
    otro_nombre_1 = models.CharField(max_length = 30)
    otro_nombre_2 = models.CharField(max_length = 30)
    ingreso_nombre_1 =  models.FloatField()
    ingreso_nombre_2 =  models.FloatField()
    apoyo_F_E = models.BooleanField()
    tipo_de_apoyo =  models.CharField(max_length = 30)
    numero_folio = models.CharField(max_length = 30)
    monto_folio =  models.FloatField()
    otro_especifique = models.CharField(max_length = 30)
    iniciativa_privada  = models.CharField(max_length = 30)
    monto_i_p =  models.FloatField()
    numero_persona_dep = models.IntegerField(default=0)
    ingreso_mensual_total = models.FloatField()
    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}{16}'.format(self.personas_que_trabajan, self.ingreso_padre, self.ingreso_madre,
        self.otro_nombre_1, self.otro_nombre_2, self.ingreso_nombre_1, self.ingreso_nombre_2, self.apoyo_F_E, self.tipo_de_apoyo, self.numero_folio,self.monto_folio, self.otro_especifique, self.iniciativa_privada,
        self.monto_i_p, self.numero_persona_dep, self.ingreso_mensual_total )

class gastoFamiliarMensual(models.Model):
    agua = models.FloatField()
    luz = models.FloatField()
    telefono = models.FloatField()
    gas = models.FloatField()
    educacion = models.FloatField()
    transporte = models.FloatField()
    renta = models.FloatField()
    television_por_cable = models.FloatField()
    internet = models.FloatField()
    otros_1 = models.FloatField()
    otros_2 = models.FloatField()
    gasto_alimentacion = models.FloatField()
    gastos_vestido = models.FloatField()
    gastos_servicios_medicos = models.FloatField()
    gasto_diversion = models.FloatField()
    otros_gastos_1 = models.FloatField()
    otros_gastos_2 = models.FloatField()
    total_gastos = models.FloatField()

    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}{16}'.format(self.agua, self.luz, self.telefono, self.gas, self.educacion, self.transporte,
         self.renta, self.television_por_cable, self.internet, self.otros_1, self.otros_2, self.gasto_alimentacion, self.gastos_vestido, self.gastos_servicios_medicos,
         self.gasto_diversion, self.otros_gastos_1, self.otros_gastos_2, self.total_gastos  )


class personasQueDependenDelIngresoMensual(models.Model):
    numero_hermanos = models.IntegerField(default=0)
    nombres_personas = models.TextField(null=True)
    edades_personas = models.TextField(null=True)
    parentescos_personas = models.TextField(null=True)
    tipo_comprobante_personas = models.TextField(null=True)
    observaciones = models.TextField(null=True)
    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}{6}'.format(self.numero_hermanos,self.nombres_personas, self.edades_personas,self.parentescos_personas, self.tipo_comprobante_personas,
        self.observaciones)



class informacionSocioEconomica(models.Model):
    casa_familiar = models.CharField(max_length = 30)
    material_paredes = models.CharField(max_length = 30)
    material_piso = models.CharField(max_length = 30)
    material_techo = models.CharField(max_length = 30)
    tipo_vivienda = models.CharField(max_length = 30)
    servicios_publicos = models.CharField(max_length = 30)
    servicios_vivienda = models.TextField(null=True)
    casa_cuenta_con = models.TextField(null=True)
    personas_habitan = models.IntegerField(default=0)
    cuartos = models.IntegerField(default=0)
    banios = models.IntegerField(default=0)
    banios_tipo = models.CharField(max_length = 30)
    cocina_tipo = models.CharField(max_length = 30)
    comedor = models.BooleanField()
    sala = models.BooleanField()
    biblioteca = models.BooleanField()
    terraza = models.BooleanField()
    cuarto_estudio = models.BooleanField()
    patio = models.BooleanField()
    cochera = models.BooleanField()
    cuarto_servicio = models.BooleanField()
    otro = models.CharField(max_length = 30)
    focos = models.CharField(max_length = 30)
    automovil = models.BooleanField()
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    anio = models.IntegerField(default=0)
    tipo_cultivo = models.CharField(max_length = 30)
    otros_bienes = models.TextField(null=True)
    negocio = models.CharField(max_length = 30)
    tipo_negocio = models.CharField(max_length = 30)
    otros_bienes_especifique = models.CharField(max_length = 30)
    servicios_asistencia_medica = models.TextField(null=True)
    otros_servicios = models.CharField(max_length = 30)
    apoyo_dependencia = models.BooleanField()
    en_especie = models.CharField(max_length = 30)
    monto_apoyo = models.FloatField()
    dependencia_empresa = models.CharField(max_length = 30)
    periodo_apoyo = models.CharField(max_length = 30)
    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}{16}{17}{18}{19}{20}{21}{22}{23}{24}{25}{26}{27}{28}{29}{30}{31}{32}{33}{34}{35}{36}{37}{38}'.format(
        self.casa_familiar, self.material_paredes, self.material_piso, self.material_techo, self.tipo_vivienda, self.servicios_publicos,
        self.servicios_vivienda, self.casa_cuenta_con, self.personas_habitan, self.cuartos, self.banios, self.banios_tipo, self.cocina_tipo,
        self.comedor, self.sala, self.biblioteca, self.terraza, self.cuarto_estudio, self.patio, self.cochera, self.cuarto_servicio,
        self.otro, self.focos, self.automovil, self.marca, self. modelo, self.anio, self. tipo_cultivo, self.otros_bienes, self.negocio,
        self.tipo_negocio, self.otros_bienes_especifique, self.servicios_asistencia_medica, self.otros_servicios, self.apoyo_dependencia,
        self.en_especie, self.monto_apoyo, self.dependencia_empresa, self.periodo_apoyo
        )
