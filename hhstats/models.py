from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from hhmain.models import TimeRegister

class Regions(TimeRegister):
    city = models.CharField(max_length=100, verbose_name="Город")
    country = models.CharField(max_length=50, verbose_name="Страна")
    region = models.CharField(max_length=150, verbose_name="Регион")
    vac_city = models.CharField(max_length=50, default=" ", verbose_name="Уникальный код города")

    def __str__(self):
        return self.country + " " + self.region + " " + self.city

    class Meta:
        ordering = ["vac_city"]
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Skills(TimeRegister):
    name = models.CharField(max_length=150, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Ключевой навык"
        verbose_name_plural = "Ключевые навыки"

class Prof_Area(TimeRegister):
    name = models.CharField(max_length=300, verbose_name="Название")

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["name"]
        verbose_name = "Профессиональная область"
        verbose_name_plural = "Профессиональные области"


class Prof_Specs(TimeRegister):
    name = models.CharField(max_length=300, verbose_name="Название")

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["name"]
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Vacancies(TimeRegister):
    name = models.CharField(max_length=200, verbose_name="Название")
    url = models.CharField(max_length=300, verbose_name="Ссылка на объявление")
    file_name = models.CharField(max_length=200, verbose_name="Имя файла с описанием")
    min_salary = models.FloatField(verbose_name="Минимальная зарплата")
    max_salary = models.FloatField(verbose_name="Максимальная зарплата")
    experience = models.IntegerField(verbose_name="Требуемый опыт")
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    prof_spec = models.ManyToManyField(Prof_Specs)
    prof_area = models.ManyToManyField(Prof_Area)


    def __str__(self):
        return self.url

    class Meta:
        ordering = ["name"]
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

