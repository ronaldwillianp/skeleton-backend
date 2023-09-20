from rest_framework import serializers
from .models import CategoriaNoticia, EstadoNoticia, Noticia, EstadoComentario, ComentarioNoticia, FAQ, EnlacesInteres, CategoriaEnlaceInteres
from apps.administracion.serializers import UserSerializer

class CategoriaNoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaNoticia
        fields = '__all__'

class EstadoNoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoNoticia
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):

    estado_info = EstadoNoticiaSerializer(read_only=True, source="estado")
    categoria_info = CategoriaNoticiaSerializer(read_only=True, many=True, source="categoria")
    creada_por_info = UserSerializer(read_only=True, source="creada_por")

    class Meta:
        model = Noticia
        fields = '__all__'

class EstadoComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoComentario
        fields = '__all__'

class ComentarioNoticiaSerializer(serializers.ModelSerializer):
    estado_info = EstadoNoticiaSerializer(read_only=True, source="estado")
    creada_por_info = UserSerializer(read_only=True, source="creada_por")
    noticia_info = NoticiaSerializer(read_only=True, source="noticia")

    class Meta:
        model = ComentarioNoticia
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class EnlacesInteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnlacesInteres
        fields = '__all__'

class CategoriaEnlaceInteresSerializer(serializers.ModelSerializer):
    enlaces = EnlacesInteresSerializer(many=True, read_only=True)
    class Meta:
        model = CategoriaEnlaceInteres
        fields = '__all__'


