from django.db import models

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
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14{15}{16}{17}{18}{19}{20}'.format(self.fecha, self.solicita_beca_alimentaria,
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
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14{15}{16}{17}{18}{19}'.format(self.gastos_mensuales, self.gastos_adicionales,
        self.cant_personas_renta, self.renta_mensual, self.cant_familiares_renta, self.parentesco_arrentador, self.medio_de_transporte,
        self.datos_transporte_propio, self.celular, self.celular_marca, self.celular_modelo,self.camara_fotografica, self.reproductor_de_audio,
        self.tableta_electronica, self.centro_de_trabajo, self.ingreso_mensual, self.datos_trabajo, self.jefe_de_familia, self.personas_dependientes)
