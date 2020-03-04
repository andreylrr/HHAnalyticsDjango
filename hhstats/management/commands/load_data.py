from django.core.management.base import BaseCommand, CommandError
from hhstats.models import Vacancies, Skills, Regions, Prof_Area, Prof_Specs
import os
import csv
from django.db import connection
import datetime

class Command(BaseCommand):
    help = 'Load data from csv files into SQLite DB'

    def add_arguments(self, parser):
        # Путь к файлам с данными
        parser.add_argument('path_to_files', nargs='+', type=str)


    def handle(self, *args, **options):

            files = ["main_prof_area_vacancies.csv", "main_prof_specs_vacancies.csv",
                     "main_regions.csv", "main_skills.csv", "main_vacancies.csv",
                     "main_prof_specs_vacancies.csv", "main_prof_area_vacancies.csv"]
            # Проверить есть ли требуемые файлы в указанном каталоге
            file_exists: bool = True
            paths = options["path_to_files"]
            for path in paths:
                for file_name in files:
                    if not os.path.isfile(path+"/"+file_name):
                        file_exists = False
                        break
            if not file_exists :
                self.stdout.write(f"Один из файлов {files} не сущеуствует в каталоге {options['path_to_files']}")
                return

            vacancy = Vacancies()
            region = Regions()
            skill = Skills()
            prof_are = Prof_Area()
            prof_spec = Prof_Specs()

            # Прочитать файл и загрузить таблицу ключевых навыков
            with open(paths[0] + "/" + "main_skills.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                   skill = Skills(id=row[0],
                                name=row[2])
                   skill.save()
            self.stdout.write(f"Таблица Ключевых навыков hhstats_skills загружена." )

            # Прочитать файл и загрузить таблицу регионов
            with open(paths[0] + "/" + "main_regions.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    region = Regions(city=row[0],
                                    country=row[1],
                                    region=row[2],
                                    vac_city=row[3],
                                    id= row[5])
                    region.save()
            self.stdout.write(f"Таблица Регионов hhstats_regions загружена." )

            # Прочитать файл и загрузить таблицу индустрий
            with open(paths[0] + "/" + "main_prof_specs.csv") as f:
                reader = csv.reader(f, delimiter=";")
                for row in reader:
                    prof_spec = Prof_Specs(id=row[0],
                                           name=row[1])
                    prof_spec.save()
            self.stdout.write(f"Таблица Индустрий hhstats_prof_specs загружена." )

            # Прочитать файл и загрузить таблицу профессиональной области
            with open(paths[0] + "/" + "main_prof_area.csv") as f:
                reader = csv.reader(f, delimiter=";")
                for row in reader:
                    prof_are = Prof_Area(id=row[0],
                                         name=row[1])
                    prof_are.save()
            self.stdout.write(f"Таблица Профессиональной области hhstats_prof_area загружена." )

            # Прочитать и загрузить таблицу вакансий
            with open(paths[0] + "/" + "main_vacancies.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    min_salary = 0 if row[4] == '' else int(row[4])
                    max_salary = 0 if row[5] == '' else int(row[5])
                    vacancy = Vacancies(
                        id=row[0],
                        name = row[1],
                        url = row[2],
                        file_name = row[3],
                        min_salary = min_salary,
                        max_salary = max_salary,
                        experience = row[9],
                        region_id = row[8])
                    vacancy.save()
            self.stdout.write(f"Таблица Вакансий hhstats_vacancies загружена." )

            # Прочитать и загрузить вспомогательную таблицу для связи вакансии с ключевыми навыками
            with open(paths[0] + "/" + "main_skills_vacancies.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    with connection.cursor() as cursor:
                        cursor.execute("""INSERT INTO hhstats_vacancies_skills (vacancies_id, skills_id) VALUES (%s,%s);""",
                            (row[0], row[1]))
                    connection.commit()
            self.stdout.write(f"Вспомогательная таблица hhstats_vacancies_skills загружена." )

            # Прочитать и загрузить вспомогательную таблицу для связи вакансии и профессианальной области
            with open(paths[0] + "/" + "main_prof_area_vacancies.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    with connection.cursor() as cursor:
                        cursor.execute("""INSERT INTO hhstats_vacancies_prof_area (vacancies_id, prof_area_id) VALUES (%s,%s);""",
                                       (row[0], row[1]))
                    connection.commit()
            self.stdout.write(f"Вспомогательная таблица hhstats_vacancies_prof_area загружена." )

            # Прочитать и загрузить вспомогательную таблицу для связи вакансии и специализации
            with open(paths[0] + "/" + "main_prof_specs_vacancies.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    with connection.cursor() as cursor:
                        cursor.execute("""INSERT INTO hhstats_vacancies_prof_spec (vacancies_id, prof_specs_id) VALUES (%s,%s);""",
                                       (row[0], row[1]))
                    connection.commit()
            self.stdout.write(f"Вспомогательная таблица hhstats_vacancies_prof_specs загружена." )


            self.stdout.write(f"База Данных восстановлена из файлов полностью.")





