from django.urls import include, path
from rest_framework import routers
from tituloprovision import views

router = routers.DefaultRouter()
router.register("facultad", views.FacultadView)
router.register("nomenclatura", views.NomenclaturaView)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/titulos/", views.NomenclaturaListView.as_view(), name="buscar"),
]
