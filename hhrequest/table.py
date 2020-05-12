from django_tables2 import SingleTableView
import django_tables2 as tables
from django_tables2.utils import A
from hhrequest.models import Requests

# Класс для отображения таблицы запросов
class RequestTable(tables.Table):
    # столбец для просмотра результатов запроса
    link_to_detail = tables.LinkColumn(
        "hhrequest:detail_request",
        accessor="__str__",
        verbose_name="Результаты",
        empty_values=(),
        text="Смотреть",
        args=[A("pk")]
    )

    def render_status(self, value):
        """
           метод для преобразования значения статуса запроса
        :param value: значение статуса из БД
        :return: преобразованное значения
        """
        if value == 0:
            return "Новый"
        elif value == 1:
            return "В обработке"
        elif value == 2:
            return "Завершен"

    def render_type(self, value):
        """
           метод для преобразования значения типа запроса
        :param value: значение типа из БД
        :return: преобразованное значения
        """
        if value == 0:
            return "Аналитика"
        elif value == 1:
            return "API"
        elif value == 2:
            return "Статистика"


    class Meta:
        # модель, которая будет использована во view
        model = Requests
        # имя template для отображения таблицы. Не путать с history.html
        template_name = "django_tables2/bootstrap4.html"
        # Список полей, которые буду выведены в таблице
        fields = ("region",
                  "text_request",
                  "file_name",
                  "status",
                  "type",
                  "vacancy_number",
                  "created",
                  "link_to_detail",
                  )

