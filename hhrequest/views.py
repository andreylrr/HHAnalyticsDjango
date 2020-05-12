from django.shortcuts import render
from HHAnalyticsDjango.settings import BASE_DIR
from .models import Requests
from .forms import RequestsForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django_tables2 import SingleTableView, RequestConfig
from .table import RequestTable
import json

# View для создания запроса и отображения сообщения
class RequestCreate(SuccessMessageMixin, CreateView):
    form_class = RequestsForm
    model = Requests
    template_name = 'requests.html'
    success_message = f'Ваш запрос сохранен в БД и направлен на обработку. Результаты запроса можно найти в Истории'

    def form_valid(self, form):
        """
           метод для обработки валидной формы
        :param form: возвращенная форма запроса
        :return: страницу с формой после обработки запроса
        """
        form.instance.user_id = 1
        form.instance.status = 0
        form.instance.vacancy_number = -1
        form.instance.type = 1
        return super(RequestCreate,self).form_valid(form)

    def get_success_message(self, cleaned_data):
        """
            метод для отображения сообщения
        :param cleaned_data:
        :return:
        """
        return self.success_message % dict(
            cleaned_data,
        )
# Класс для отображения таблицы с историей запросово
class RequestsListView(SingleTableView):
    table_class = RequestTable
    model = Requests
    table_pagination = False
    template_name = "history.html"

# Класс для отображения детальной информации о запросе
class RequestDetailView(DetailView):
    template_name = "request-view.html"
    model = Requests
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        """
            Метод для формирования контекста страницы
        :param kwargs:
        :return: контекст
        """
        # Вызов метода для формирования контекста родительского класса
        context = super(RequestDetailView, self).get_context_data(**kwargs)
        # Достаем из БД имя файла с результатами обработки запроса
        pk = self.kwargs['pk']
        # находим запись о запросе в БД
        row = Requests.objects.filter(id=pk).first()
        if row.file_name is not None:
            # формируем путь к файлу с результатами запроса
            file_name = BASE_DIR + "/Helpers/ParserHHApi/" + row.file_name
            # Читаем результаты обработки запроса из файла
            with open(file_name, "r") as f:
                result: json = json.load(f)
            # Обрабатываем результаты запроса
            description_skills: dict = result['description']
            key_skills: dict = result['keyskills']
            salary_average: dict = result['salary']
            # Для навыков из описания
            sum_description: list = []
            for key, value in list(description_skills.items())[:10]:
                sum_description.append( key + " - " + str(value) + "%")
            # Для навыков из ключевых навыков
            sum_keyskills: list = []
            for key, value in list(key_skills.items())[:10]:
                sum_keyskills.append(key + " - " + str(value) + "%")
            sum_salaries: list = []
            # Для зарплат
            for key, value in salary_average.items():
                sum_salaries.append(key + "   от: " + '{:6.0f}'.format(value[0]) + "₽.  до: " + '{:6.0f}'.format(value[1]) + "₽.")

            # сохраняем извлеченные данные в контексте
            context['sum_descriptions'] = sum_description
            context['sum_keyskills'] = sum_keyskills
            context['sum_salaries'] = sum_salaries

        return context
