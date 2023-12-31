from django.db import models
from apps.administracion.models import User

# Create your models here.

class CategoriaNoticia(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class EstadoNoticia(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False)
    portada = models.ImageField(upload_to='imagenes/portadas', null=True, blank=True)
    subtitulo = models.TextField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    creada_por = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    categoria = models.ManyToManyField(CategoriaNoticia)
    estado = models.ForeignKey(EstadoNoticia, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.titulo

class EstadoComentario(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nombre

class ComentarioNoticia(models.Model):
    comentario = models.TextField(null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creada_por = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    noticia = models.ForeignKey(Noticia, on_delete=models.PROTECT, null=False, blank=False)
    estado = models.ForeignKey(EstadoComentario, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.comentario

class FAQ(models.Model):
    pregunta = models.CharField(max_length=255, null=False, blank=False)
    respuesta = models.TextField(null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pregunta

class CategoriaEnlaceInteres(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class EnlacesInteres(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    enlace = models.URLField(null=False, blank=False)
    categoria = models.ForeignKey(CategoriaEnlaceInteres, on_delete=models.PROTECT, null=False, blank=False, related_name="enlaces")

    def __str__(self):
        return self.nombre

class Imagen(models.Model):
    imagen = models.ImageField()

class Coleccion(models.Model):
    titulo = models.CharField(max_length=250, blank =True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    imagenes = models.ManyToManyField(Imagen, null=False, blank=False)
