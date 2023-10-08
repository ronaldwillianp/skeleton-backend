from rest_framework import serializers
from .models import Empresa, Socio, Servicio, Directivo

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class DirectivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directivo
        fields = '__all__'