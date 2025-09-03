from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .models import Persona, Tarea
from .serializers import PersonaSerializer, TareaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar Personas.
    """
    queryset = Persona.objects.all().order_by("id_persona")
    serializer_class = PersonaSerializer

    @action(detail=False, methods=['get'], url_path='filtrar')
    def filtrar(self, request):
        """
        Filtra personas por número de documento.
        GET /api/personas/filtrar/?documento=123456
        """
        documento = request.query_params.get('documento')
        if documento:
            personas = self.queryset.filter(documento=documento)
            serializer = self.get_serializer(personas, many=True)
            return Response(serializer.data)
        return Response({"error": "Se requiere el parámetro 'documento'."}, status=status.HTTP_400_BAD_REQUEST)


class TareaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar Tareas.
    """
    queryset = Tarea.objects.all().order_by("id_tarea")
    serializer_class = TareaSerializer

    @action(detail=False, methods=['get'], url_path='filtrar')
    def filtrar(self, request):
        """
        Filtro de tareas:
        - fecha_limite=YYYY-MM-DD
        - fecha_inicio=YYYY-MM-DD&fecha_fin=YYYY-MM-DD
        - tipo_documento=CC&documento_persona=123456
        """
        tareas = self.queryset
        fecha = request.query_params.get('fecha_limite')
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        tipo_doc = request.query_params.get('tipo_documento')
        documento_persona = request.query_params.get('documento_persona')

        if fecha:
            tareas = tareas.filter(fecha_limite=fecha)
        if fecha_inicio and fecha_fin:
            tareas = tareas.filter(fecha_limite__range=(fecha_inicio, fecha_fin))
        if tipo_doc and documento_persona:
            tareas = tareas.filter(persona__tipo_documento=tipo_doc, persona__documento=documento_persona)

        serializer = self.get_serializer(tareas, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def api_root(request, format=None):
    """
    Vista raíz de la API que muestra los recursos disponibles.
    """
    return Response({
        "personas": request.build_absolute_uri("personas/"),
        "tareas": request.build_absolute_uri("tareas/"),
    })
