from rest_framework import routers
from .viewsets import EmpresaViewSet

router = routers.SimpleRouter()
router.register('empresa', EmpresaViewSet)
urlpatterns = router.urls