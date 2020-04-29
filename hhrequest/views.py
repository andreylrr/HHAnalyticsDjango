from django.shortcuts import render
from .models import Requests
from .forms import RequestsForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


def hhrequest(request):
    return render(request, 'requests.html')

def history(request):
    return render(request, 'history.html')

class RequestCreate(SuccessMessageMixin, CreateView):
    form_class = RequestsForm
    model = Requests
    template_name = 'requests.html'
    success_message = f'Ваш запрос сохранен в БД и направлен на обработку. Результаты запроса можно найти в Истории'

    def form_valid(self, form):
        form.instance.user_id = 1
        form.instance.status = 0
        form.instance.vacancy_number = -1
        return super(RequestCreate,self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
        )
