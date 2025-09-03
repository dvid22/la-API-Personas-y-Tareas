# Documentación del Proyecto: API de Personas y Tareas

## 1. Descripción del Proyecto

Este proyecto consiste en una API REST desarrollada con **Django y Django REST Framework (DRF)** para gestionar:

- **Personas**: CRUD completo y filtrado por número de documento.  
- **Tareas**: CRUD completo, filtrado por fecha límite, rango de fechas y persona asignada.

La API permite la integración con aplicaciones front-end o clientes externos mediante **JSON**.

---

## 2. Endpoints Principales

### API Root

- **Método:** GET  
- **URL:** `/`  
- **Descripción:** Devuelve los endpoints principales de la API.  
- **Response ejemplo:**
```json
{
    "personas": "http://127.0.0.1:8000/personas/",
    "tareas": "http://127.0.0.1:8000/tareas/"
}

Personas
Acción	Método	URL	Descripción
Listar	GET	/personas/	Lista todas las personas
Crear	POST	/personas/	Crea una nueva persona
Detalle	GET	/personas/{id}/	Obtiene los datos de una persona por ID
Actualizar	PUT/PATCH	/personas/{id}/	Actualiza una persona
Eliminar	DELETE	/personas/{id}/	Elimina una persona
Filtrar	GET	/personas/filtrar/?documento={documento}	Filtra personas por número de documento
Tareas
Acción	Método	URL	Descripción
Listar	GET	/tareas/	Lista todas las tareas
Crear	POST	/tareas/	Crea una nueva tarea
Detalle	GET	/tareas/{id}/	Obtiene los datos de una tarea por ID
Actualizar	PUT/PATCH	/tareas/{id}/	Actualiza una tarea
Eliminar	DELETE	/tareas/{id}/	Elimina una tarea
Filtrar por fecha	GET	/tareas/filtrar/?fecha_limite={YYYY-MM-DD}	Filtra tareas por fecha límite exacta
Filtrar por rango	GET	/tareas/filtrar/?fecha_inicio={YYYY-MM-DD}&fecha_fin={YYYY-MM-DD}	Filtra tareas por rango de fechas
Filtrar por persona	GET	/tareas/filtrar/?tipo_documento={tipo}&documento_persona={documento}	Filtra tareas asignadas a una persona
3. Ejemplos de Request y Response
Crear Persona
POST /personas/
Content-Type: application/json

{
    "tipo_documento": "CC",
    "documento": "12345678",
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan@example.com",
    "activo": true
}


Response:

{
    "id_persona": 1,
    "tipo_documento": "CC",
    "documento": "12345678",
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan@example.com",
    "activo": true
}

Filtrar tareas por rango de fechas
GET /tareas/filtrar/?fecha_inicio=2025-09-01&fecha_fin=2025-09-10


Response ejemplo:

[
    {
        "id_tarea": 1,
        "titulo": "Hacer reporte",
        "descripcion": "Reporte de ventas",
        "fecha_limite": "2025-09-05",
        "persona": 1
    }
]

4. Postman

La colección de Postman con todos los endpoints está disponible en el siguiente enlace:

https://serniet22-6135841.postman.co/workspace/Sergio-Nieto's-Workspace~0dc71281-47ce-40c6-8b57-47159d18c6d9/collection/48003272-1d179ccd-ffb4-4aaf-b798-520f567b9e0e?action=share&creator=48003272