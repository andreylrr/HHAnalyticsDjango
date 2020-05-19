from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from hhmain.models import TimeRegister

# класс для определения модели регионов
class Regions(TimeRegister):
    # название города
    city = models.CharField(max_length=100, verbose_name="Город")
    # название страны
    country = models.CharField(max_length=50, verbose_name="Страна")
    # название региона
    region = models.CharField(max_length=150, verbose_name="Регион")
    # код местоположения
    vac_city = models.CharField(max_length=50, default=" ", verbose_name="Уникальный код города")

    def __str__(self):
        return self.country + " " + self.region + " " + self.city

    class Meta:
        ordering = ["vac_city"]
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

# класс для определения модели ключевых навыков
class Skills(TimeRegister):
    # название ключевого навыка
    name = models.CharField(max_length=150, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Ключевой навык"
        verbose_name_plural = "Ключевые навыки"

# класс для определения модели профессиональной области
class Prof_Area(TimeRegister):
    # название профессионального навыка
    name = models.CharField(max_length=300, verbose_name="Название")

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["name"]
        verbose_name = "Профессиональная область"
        verbose_name_plural = "Профессиональные области"

# класс для определения модели специализации
class Prof_Specs(TimeRegister):
    # название специализации
    name = models.CharField(max_length=300, verbose_name="Название")

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["name"]
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"

# класс для определения модели вакансий
class Vacancies(TimeRegister):
    # название вакансии
    name = models.CharField(max_length=200, verbose_name="Название")
    # ссылка на объявление о вакансии
    url = models.CharField(max_length=300, verbose_name="Ссылка на объявление")
    # имя файла, в котором находится информация о вакансии
    file_name = models.CharField(max_length=200, verbose_name="Имя файла с описанием")
    # минимальная зарплата
    min_salary = models.FloatField(verbose_name="Минимальная зарплата")
    # максимальная зарплата
    max_salary = models.FloatField(verbose_name="Максимальная зарплата")
    # валюта зарплаты
    currency = models.CharField(max_length=5, verbose_name="Валюта зарплаты")
    # стаж в годах
    experience = models.IntegerField(verbose_name="Требуемый опыт")
    # ссылка на таблицу регионов
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    # ссыслка на таблицу ключевых навыков
    skills = models.ManyToManyField(Skills)
    # ссылка на таблицу специализаций
    prof_spec = models.ManyToManyField(Prof_Specs)
    # ссылка на таблицу профессиональных областей
    prof_area = models.ManyToManyField(Prof_Area)


    def __str__(self):
        return self.url

    class Meta:
        ordering = ["name"]
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

