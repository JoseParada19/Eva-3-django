from django.db import models
from peliculas.models import Pelicula
from clientes.models import Cliente

class Entrada(models.Model):

    codigo_entrada = models.CharField(max_length=50, unique=True)
    hora = models.TimeField()
    fecha = models.DateField()
    butaca = models.CharField(max_length=10)
    sala = models.CharField(max_length=50)
    nombre_cine = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='entradas')
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='entradas')

    def __str__(self):
        return f"Entrada {self.codigo_entrada} - Cliente: {self.cliente}, Película: {self.pelicula}"

