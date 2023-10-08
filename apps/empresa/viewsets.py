from rest_framework import viewsets
from .serializers import *

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class DirectivoViewSet(viewsets.ModelViewSet):
    queryset = Directivo.objects.all()
    serializer_class = DirectivoSerializer