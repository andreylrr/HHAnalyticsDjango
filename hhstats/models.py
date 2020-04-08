from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Regions(models.Model):
    city = models.CharField(max_length=50, verbose_name="Город")
    country = models.CharField(max_length=50, verbose_name="Страна")
    region = models.CharField(max_length=100, verbose_name="Регион")
    vac_city = models.CharField(max_length=50, default=" ", verbose_name="Уникальный код города")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return self.country + " " + self.region + " " + self.city

    class Meta:
        ordering = ["vac_city"]
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Skills(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Ключевой навык"
        verbose_name_plural = "Ключевые навыки"

class Prof_Area(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["name"]
        verbose_name = "Профессиональная область"
        verbose_name_plural = "Профессиональные области"


class Prof_Specs(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["name"]
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Vacancies(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    url = models.CharField(max_length=300, verbose_name="Ссылка на объявление")
    file_name = models.CharField(max_length=200, verbose_name="Имя файла с описанием")
    min_salary = models.FloatField(verbose_name="Минимальная зарплата")
    max_salary = models.FloatField(verbose_name="Максимальная зарплата")
    experience = models.IntegerField(verbose_name="Требуемый опыт")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
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




