from django.db import models

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__ (self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__ (self):
        return self.nombre

class Aprendiz (models.Model):
    nombre = models.CharField(max_length=250)
    edad = models.PositiveIntegerField()
    vivo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='aprendiz', null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    rol = models.ManyToManyField(Rol, null=True, blank=True)

    def __str__ (self):
        return self.nombre
