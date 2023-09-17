from rest_framework import routers
from .viewsets import CategoriaNoticiaViewSet, EstadoNoticiaViewSet, NoticiaViewSet, EstadoComentarioViewSet, ComentartioNoticiaViewSet, FAQViewSet, EnlacesInteresViewSet, CategoriaEnlaceInteresViewSet

router = routers.SimpleRouter()
router.register('categoria_noticia', CategoriaNoticiaViewSet)
router.register('estado_noticia', EstadoNoticiaViewSet)
router.register('noticia', NoticiaViewSet)
router.register('estado_comentario', EstadoComentarioViewSet)
router.register('comentario_noticia', ComentartioNoticiaViewSet)
router.register('faq', FAQViewSet)
router.register('categoria_enlace_interes', CategoriaEnlaceInteresViewSet)
router.register('enlace_interes', EnlacesInteresViewSet)
urlpatterns = router.urls
