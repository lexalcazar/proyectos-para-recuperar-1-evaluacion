import uuid
from django.db import models

# Create your models here.
# Modelo para representar un instrumento musical
class Instrumento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.precio})"
#Modelo para representar una categoría de instrumentos
class Categoria(models.Model):
    #selecionar famila de instrumentos entre unas ya marcadas
    FAMILIA_INSTRUMENTOS = [
        ('cuerda', 'Cuerda'),
        ('viento', 'Viento'),
        ('percusion', 'Percusión'),
        ('teclado', 'Teclado'),
    ]
    TIPO_INSTRUMENTO=[
        ('acustico', 'Acústico'),
        ('electrico', 'Eléctrico'),
        ('digital', 'Digital'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    familia = models.CharField(max_length=100, choices=FAMILIA_INSTRUMENTOS, default='cuerda')
    descripcion = models.TextField()
    tipo = models.CharField(max_length=100, choices=TIPO_INSTRUMENTO, default='acustico')
    def __str__(self):
        return self.nombre

#Modelo para representar una marca de instrumentos
class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre