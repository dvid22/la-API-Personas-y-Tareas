from django.db import models

class Persona(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ("CC", "Cédula de ciudadanía"),
        ("TI", "Tarjeta de identidad"),
        ("CE", "Cédula de extranjería"),
        ("PP", "Pasaporte"),
    ]

    id_persona = models.AutoField(
        primary_key=True,
        editable=False,
        db_column='T001idpersona'
    )
    tipo_documento = models.CharField(
        max_length=2,
        choices=TIPO_DOCUMENTO_CHOICES,
        db_column='T001TipoDocumento',
        default="CC"
    )
    documento = models.CharField(
        max_length=20,
        unique=True,
        db_column='T001Documento',
        default="0000000000"
    )
    nombre = models.CharField(
        max_length=100,
        db_column='T001Nombre',
        default="NombreDesconocido"
    )
    apellido = models.CharField(
        max_length=100,
        db_column='T001Apellido',
        default="ApellidoDesconocido"
    )
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True
    )
    activo = models.BooleanField(
        default=True,
        db_column='T001Activo'
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.tipo_documento}-{self.documento})"

    class Meta:
        db_table = 'T001Persona'
        verbose_name = 'persona'
        verbose_name_plural = 'personas'


class Tarea(models.Model): 
    id_tarea = models.AutoField(
        primary_key=True,
        editable=False,
        db_column='T002IdTarea'
    )
    titulo = models.CharField(
        max_length=200,
        db_column='T002Titulo',
        default="Sin título"
    )
    descripcion = models.TextField(
        null=True,
        blank=True,
        default=""
    )
    fecha_limite = models.DateField(
        db_column='T002FechaLimite',
        null=True,
        blank=True
    )
    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='tareas',
        db_column='T002PersonaId',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.titulo} (para {self.persona.nombre if self.persona else 'Sin asignar'})"

    class Meta:
        db_table = 'T002Tarea'
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
