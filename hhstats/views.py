from .forms import StatsRequestsForm
from hhrequest.models import Requests
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

# Класс для формирования запроса по статистике конкретного региона
class StatsRequestCreate(SuccessMessageMixin, CreateView):
    form_class = StatsRequestsForm
    model = Requests
    template_name = "stats-request.html"
    success_message = f'Ваш запрос сохранен в БД и направлен на обработку. Результаты запроса можно найти в Истории'

    def form_valid(self, form):
        """
            метод для обработки валидной формы
        :param form:
        :return:
        """
        form.instance.user_id = 1
        form.instance.status = 0
        form.instance.vacancy_number = -1
        form.instance.type = 2
        return super(StatsRequestCreate, self).form_valid(form)

    def get_success_message(self, cleaned_data ):
        """
            метод для вывода сообщения об успешной записи запроса по статистике региона
        :param cleaned_data:
        :return:
        """
        return self.success_message % dict(
            cleaned_data,
        )
