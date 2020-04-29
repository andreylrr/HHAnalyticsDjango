from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactsForm
from .models import Contacts
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
import datetime


def main_page(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

def register(request):
    return render(request, 'register.html')

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
