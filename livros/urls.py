
from rest_framework import routers
from livros.views import livrosViewSet

router = routers.DefaultRouter()
router.register(r'', livrosViewSet)

urlpatterns = router.urls