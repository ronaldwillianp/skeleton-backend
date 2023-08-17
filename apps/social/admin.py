from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.EstadoNoticia)
admin.site.register(models.CategoriaNoticia)
admin.site.register(models.Noticia)