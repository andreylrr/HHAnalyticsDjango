from .forms import StatsRequestsForm
from hhrequest.models import Requests
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Класс для формирования запроса по статистике конкретного региона
class StatsRequestCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = StatsRequestsForm
    model = Requests
    template_name = "stats-request.html"
    success_message = f'Ваш запрос сохранен в БД и направлен на обработку. Результаты запроса можно найти в Истории'
    login_url = reverse_lazy("hhmain:login")

    def form_valid(self, form):
        """
            метод для обработки валидной формы
        :param form:
        :return:
        """
        form.instance.user_id = self.request.user.id
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
