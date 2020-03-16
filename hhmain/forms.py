from django import forms
from .models import Contacts

class ContactsForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields =('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control text-center text-info text-gray-900"}),
            'email': forms.EmailInput(attrs={'class': "form-control text-center text-gray-900"}),
            'content': forms.Textarea(attrs={'class': "form-control text-center text-info text-gray-900 row=50"})
        }
