from django.db import models

class Pelicula(models.Model):
    nombre_pelicula = models.CharField(max_length=100)
    duracion_pelicula = models.DurationField()
    fecha_estreno = models.DateField()
    genero = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=10)
    tipo_pelicula = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_pelicula
