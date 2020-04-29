from django.db import models
from hhmain.models import TimeRegister
from django.urls import reverse

class Requests(TimeRegister):
    user_id = models.IntegerField()
    region = models.CharField(max_length=200, verbose_name="Регион")
    text_request = models.CharField(max_length=200, verbose_name="Текст")
    file_name = models.CharField(max_length=250, verbose_name="Имя файла")
    status = models.IntegerField(verbose_name="Статус")
    vacancy_number = models.IntegerField(verbose_name="Колличество вакансий")

    def __str__(self):
        return f"{self.region} {self.text_request} {self.user_id}"

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"

    def get_absolute_url(self):
        if self.text_request :
            url_request = 'hhrequest:request'
        else:
            url_request = 'hhstat:stats-request'
        return reverse(url_request)
