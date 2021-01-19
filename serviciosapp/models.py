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
        return '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14{15}{16}{17}{18}{19}{20}'.format(self.fecha, self.solicita_beca_alimentaria, self.ap_paterno, self.ap_materno, self.nombre
        , self.sexo, self.edad, self.estado_civil, self.carrera, self.semestre, self.grupo, self.telefono
        , self.otro_idiona, self.residencia_distinta, self.calle, self.numero, self.colonia, self.municipio
        , self.estado, self.propietario, self.parentesco)
