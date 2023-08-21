from rest_framework import serializers
from .models import CategoriaNoticia, EstadoNoticia, Noticia, EstadoComentario, ComentartioNoticia, FAQ, EnlacesInteres
class CategoriaNoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaNoticia
        fields = '__all__'
class EstadoNoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoNoticia
        fields = '__all__'
class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

class EstadoComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoComentario
        fields = '__all__'

class ComentartioNoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentartioNoticia
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class EnlacesInteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnlacesInteres
        fields = '__all__'

