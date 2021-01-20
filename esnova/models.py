from django.db import models
class Articulo(models.Model):
    articulo = models.CharField(max_length = 50)
    def __str__(self):
        return '{0}'.format(self.articulo)

class Alumno(models.Model):
    nombre = models.CharField(max_length = 50)
    articulos = models.ManyToManyField(Articulo)
    def __str__(self):
        return '{0}'.format(self.nombre)
