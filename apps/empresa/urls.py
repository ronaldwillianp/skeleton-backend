from rest_framework import routers
from .viewsets import EmpresaViewSet, SocioViewSet, ServicioViewSet, DirectivoViewSet

router = routers.SimpleRouter()
router.register('empresa', EmpresaViewSet)
router.register('socio', SocioViewSet)
router.register('servicio', ServicioViewSet)
router.register('directivo', DirectivoViewSet)
urlpatterns = router.urls