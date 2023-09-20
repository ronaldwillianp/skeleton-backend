from rest_framework import viewsets
from .serializers import *

class CategoriaNoticiaViewSet(viewsets.ModelViewSet):
    queryset = CategoriaNoticia.objects.all()
    serializer_class = CategoriaNoticiaSerializer

class EstadoNoticiaViewSet(viewsets.ModelViewSet):
    queryset = EstadoNoticia.objects.all()
    serializer_class = EstadoNoticiaSerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class EstadoComentarioViewSet(viewsets.ModelViewSet):
    queryset = EstadoComentario.objects.all()
    serializer_class = EstadoComentarioSerializer

class ComentarioNoticiaViewSet(viewsets.ModelViewSet):
    queryset = ComentarioNoticia.objects.all()
    serializer_class = ComentarioNoticiaSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class CategoriaEnlaceInteresViewSet(viewsets.ModelViewSet):
    queryset = CategoriaEnlaceInteres.objects.all()
    serializer_class = CategoriaEnlaceInteresSerializer

class EnlacesInteresViewSet(viewsets.ModelViewSet):
    queryset = EnlacesInteres.objects.all()
    serializer_class = EnlacesInteresSerializer
