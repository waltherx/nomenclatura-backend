from django.db import models

# Create your models here.


class Facultad(models.Model):
    nombre = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return self.nombre


class Nomenclatura(models.Model):
    NIVELES = [
        ("LICENCIATURA", "LICENCIATURA"),
        ("TECNICO SUPERIOR", "TECNICO SUPERIOR"),
        ("TECNICO MEDIO", "TECNICO MEDIO"),
    ]
    plan_carrera = models.CharField(blank=False, max_length=8)
    nombre_carrera = models.CharField(blank=False, max_length=60)
    codigo_titulo = models.CharField(blank=False, max_length=20)
    descripcion_titulo = models.CharField(blank=False, max_length=200)
    nivel = models.CharField(max_length=20, choices=NIVELES)
    estado = models.CharField(blank=False, max_length=1)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nomencaltura : {self.nombre_carrera, self.nivel}"
