from rest_framework import routers

from .views import WomenViewSet

router = routers.DefaultRouter()
router.register(r'women', WomenViewSet,
                basename='women')
