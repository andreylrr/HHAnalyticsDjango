from django.shortcuts import render, redirect
from .forms import ContactsForm, HHUserCreationForm, HHLoginForm
from .models import Contacts
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


def main_page(request):
    return render(request, 'index.html')

# View для авторизации пользователя
class HHLogin(LoginView):
    form_class = HHLoginForm
    model = User
    template_name = "login.html"
    success_url = reverse_lazy("hhmain:index")
    redirect_authenticated_user = True

    def form_valid(self, form):
        return super(HHLogin, self).form_valid(form)

# View для завершения работы с сайтом
class HHLogout(LoginRequiredMixin, LogoutView):
    login_url = reverse_lazy("hhmain:login")
    template_name = "logout.html"
    model = User

    def post(self, request):
        return render(request, 'index.html')

# View для создания обращения пользователя
class ContactsCreate(SuccessMessageMixin, CreateView):
    form_class = ContactsForm
    model = Contacts
    template_name = 'contacts.html'
    success_message = f'Ваше обращение сохранено и направлено на обработку.'

    def form_valid(self, form):
        return super(ContactsCreate, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
        )

# View для регистрации пользователя
class UserRegister(CreateView):
    form_class=HHUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "register.html"

    def form_valid(self, form):
        return super(UserRegister, self).form_valid(form)
