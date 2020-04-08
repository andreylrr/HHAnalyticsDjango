from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.EmailField(max_length=200, verbose_name="Адрес электронной почты")
    content = models.TextField(max_length=1000, verbose_name="Текст обращения")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата обращения")

    def __str__(self):
        return str(self.name) + str(self.email)

    class Meta:
        ordering = ["created"]
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
