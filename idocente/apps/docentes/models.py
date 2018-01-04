from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Cursos(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    ESTADO_CHOICES = (
        (1, 'Activo'),
        (2, 'Inactivo'),
        (3, 'Descontinuado'),
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True, default=None)
    precio = models.DecimalField(max_digits=7, decimal_places=3)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, help_text="Categoria del producto")
    insumo = models.ManyToManyField(Insumo, blank=True)
    estado = models.PositiveIntegerField(choices=ESTADO_CHOICES, blank=True, null=True, default=None)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre