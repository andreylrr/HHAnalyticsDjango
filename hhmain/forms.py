from django import forms
from .models import Contacts

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields =('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control form-control-user"}),
            'email': forms.EmailInput(attrs={'class': "form-control form-control-user"}),
            'content': forms.Textarea(attrs={'class': "form-control  row=50"})
        }
