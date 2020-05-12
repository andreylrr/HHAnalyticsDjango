from django import forms
from .models import Contacts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields =('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control form-control-user"}),
            'email': forms.EmailInput(attrs={'class': "form-control form-control-user"}),
            'content': forms.Textarea(attrs={'class': "form-control  row=50"})
        }


class HHUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(HHUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['username'].widget.attrs['placeholder'] = "Введите имя пользователя"
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password1'].widget.attrs['placeholder'] = "Введите пароль"
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password2'].widget.attrs['placeholder'] = "Введите пароль еще раз"
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес электронной почты'


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(HHUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class HHLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(HHLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['username'].widget.attrs['placeholder'] = "Введите имя пользователя"
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['placeholder'] = "Введите пароль"

    class Meta:
        model = User
        fields = ("username", "password")
