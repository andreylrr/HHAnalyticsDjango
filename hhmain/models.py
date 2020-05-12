from django.db import models
from django.urls import reverse

# Класс для добавления времени, когда происходили изменения в записи таблицы
class TimeRegister(models.Model):
    # время создания строки в таблице
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # время изменения строки в таблице
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Дата изменения")
    class Meta:
        abstract = True

# Модель таблицы Контакты
class Contacts(TimeRegister):
    # имя обращающегося
    name = models.CharField(max_length=200, verbose_name="Имя")
    # адрес электронной почты обращающегося
    email = models.EmailField(max_length=200, verbose_name="Адрес электронной почты")
    # текст обращения
    content = models.TextField(max_length=1000, verbose_name="Текст обращения")

    def __str__(self):
        return str(self.name) + str(self.email)

    class Meta:
        ordering = ["created"]
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"

    def get_absolute_url(self):
        return reverse('hhmain:contacts')
