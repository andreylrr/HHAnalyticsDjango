from django.shortcuts import render, redirect
from .forms import ContactsForm, HHUserCreationForm
from .models import Contacts
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
import datetime

# Все view использующие пользователя будут имплементированы в следующей версии
def main_page(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

def register(request):
    return render(request, 'register.html')

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

class UserRegister(CreateView):
    form_class=HHUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "register.html"

    def form_valid(self, form):
        return super(UserRegister, self).form_valid(form)