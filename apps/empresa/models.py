from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    alias = models.CharField(max_length=150, null=True, blank=True, )
    logo = models.ImageField(upload_to='empresa/logos', null=True, blank=True)
    telefono = models.CharField(max_length=8, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    correo  = models.EmailField(max_length=50, null=False, blank=False)
    director = models.CharField(max_length=150, null=True, blank=True)
    slogan = models.CharField(max_length=255, null=True, blank=True)
    video_institucional = models.FileField(null=True, blank=True)
    resumen = models.TextField(null=True, blank=True)
    facebook = models.CharField(max_length=150, null=True, blank=True)
    youtube = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.nombre

class SoporteTecnico(models.Model):
    correo = models.EmailField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Socio(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    logo = models.ImageField(upload_to='socio/fotos', null=True, blank=True)
    web = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre

