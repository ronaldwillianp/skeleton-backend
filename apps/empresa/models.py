from django.db import models


# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    logo = models.ImageField(upload_to='empresa/logos')
    telefono = models.CharField(max_length=8, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    director = models.CharField(max_length=50, null=True, blank=True)
    slogan = models.CharField(max_length=255, null=True, blank=True)
    video_institucional = models.FileField(null=True, blank=True)
    resumen = models.TextField(null=True, blank=True)
    facebook = models.CharField(max_length=150, null=True, blank=True)
    youtube = models.CharField(max_length=150, null=True, blank=True)


