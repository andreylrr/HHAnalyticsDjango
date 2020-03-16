from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactsForm
import datetime


def main_page(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def contacts(request):

    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.created = datetime.datetime.now()
            contact.save()
            return redirect('hhmain:index')
    else:
        form = ContactsForm()

    data = dict()
#    messages.success(request, "Success: This is the sample success Flash message.")
    return render(request, 'contacts.html', {'form': form, 'data': data})

def forgot_password(request):
    return render(request, 'forgot-password.html')

def register(request):
    return render(request, 'register.html')
