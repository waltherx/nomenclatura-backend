from django.contrib import admin
from tituloprovision.models import Nomenclatura, Facultad

admin.site.site_header = "Admin Nomenclaturas"
admin.site.site_title = "UAGRM"
admin.site.index_title = "Bienvenidos 😃"


class FacultadAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    list_display_links = ("id", "nombre")


class NomenclaturaAdmin(admin.ModelAdmin):
    list_display = (
        "plan_carrera",
        "nombre_carrera",
        "codigo_titulo",
        "descripcion_titulo",
        "nivel",
        "facultad",
    )
    list_display_links = (
        "plan_carrera",
        "nombre_carrera",
        "codigo_titulo",
    )
    search_fields = ("plan_carrera", "codigo_titulo", "nombre_carrera")
    list_filter = (
        "nivel",
        "estado",
    )
    list_per_page = 25


admin.site.register(Facultad, FacultadAdmin)
admin.site.register(Nomenclatura, NomenclaturaAdmin)
