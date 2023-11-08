from django.contrib import admin
from tituloprovision.models import Nomenclatura, Facultad


class NomenclaturaAdmin(admin.ModelAdmin):
    list_display = ("plan_carrera", "nombre_carrera", "descripcion_titulo", "facultad")


admin.site.register(Facultad)
admin.site.register(Nomenclatura, NomenclaturaAdmin)
