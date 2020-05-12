from django.db import models
from hhmain.models import TimeRegister
from django.urls import reverse

# Модель таблицы Requests
class Requests(TimeRegister):
    # Id пользователя, который создал запрос
    user_id = models.IntegerField()
    # Регион, заданный пользователем
    region = models.CharField(max_length=200, verbose_name="Регион")
    # Текст запроса
    text_request = models.CharField(max_length=200, verbose_name="Текст")
    # Имя файла с результатами запроса
    file_name = models.CharField(max_length=250, verbose_name="Имя файла")
    # Статус запроса
    status = models.IntegerField(verbose_name="Статус")
    # Тип запроса
    type = models.IntegerField(verbose_name="Тип")
    # колличество вакансий найденных по запросу
    vacancy_number = models.IntegerField(verbose_name="Вакансий")

    def __str__(self):
        return f"{self.region} {self.text_request} {self.user_id}"

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"
        ordering = ["-created"]


    def get_absolute_url(self):
        if self.text_request :
            url_request = 'hhrequest:request'
        else:
            url_request = 'hhstats:stats-request'
        return reverse(url_request)
