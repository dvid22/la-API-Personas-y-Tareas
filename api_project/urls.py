from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app.views import PersonaViewSet, TareaViewSet, api_root

router = DefaultRouter()
router.register(r'personas', PersonaViewSet, basename="persona")
router.register(r'tareas', TareaViewSet, basename="tarea")

urlpatterns = [
    path('', api_root, name='api-root'),       # Vista inicial de la API
    path('', include(router.urls)),            # Endpoints de Personas y Tareas
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Login de DRF
]
