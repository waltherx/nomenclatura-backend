from csv import DictReader
import csv

from django.core.management import BaseCommand

from tituloprovision.models import Facultad, Nomenclatura

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from children.csv"

    def handle(self, *args, **options):
        print("Loading....")

        # for row in DictReader(open("./datos.csv")):
        # print(row["Nombre"])
        # child = Nomenclatura(name=row["Name"], sex=row["Sex"], age=row["Age"])
        #    child.save()
        with open("nomens.csv", newline="", encoding="utf-8") as File:
            reader = csv.reader(File)
            for row in reader:
                facul = Facultad.objects.get(pk=int(row[6]))
                nomencaltura = Nomenclatura(
                    plan_carrera=row[0],
                    nombre_carrera=row[1],
                    codigo_titulo=row[2],
                    descripcion_titulo=row[3],
                    nivel=row[4],
                    estado=row[5],
                    facultad=facul,
                )
                nomencaltura.save()
