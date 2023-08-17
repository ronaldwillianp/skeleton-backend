from rest_framework import routers
from .viewsets import UserViewSet, GroupViewSet

router = routers.SimpleRouter()
router.register('user', UserViewSet)
router.register('group', GroupViewSet)
urlpatterns = router.urls