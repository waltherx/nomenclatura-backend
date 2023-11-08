import graphene
from graphene_django import DjangoObjectType
from .models import Nomenclatura, Facultad


class FacultadesType(DjangoObjectType):
    class Meta:
        model = Facultad
        fields = ("id", "nombre")


class NomenclaturasType(DjangoObjectType):
    class Meta:
        model = Nomenclatura
        fields = "__all__"


class Query(graphene.ObjectType):
    nomenclaturas = graphene.List(NomenclaturasType)
    nomenclatura = graphene.Field(NomenclaturasType, id=graphene.ID())

    facultades = graphene.List(FacultadesType)
    facultad = graphene.Field(FacultadesType, id=graphene.ID())

    def resolve_facultades(root, info):
        return Facultad.objects.all()

    def resolve_facultad(root, info, id):
        return Facultad.objects.get(id=id)

    def resolve_nomenclaturas(root, info):
        return Nomenclatura.objects.all()

    def resolve_nomenclatura(root, info, id):
        return Nomenclatura.objects.get(id=id)


schema = graphene.Schema(query=Query)
