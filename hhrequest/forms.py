from django import forms
from .models import Requests

# Форма для создания запросов
class RequestsForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ('region', 'text_request',)
        widgets = {
            'region': forms.TextInput(attrs={'class': "form-control form-control-user", 'placeholder': "Регион"}),
            'text_request': forms.TextInput(attrs={'class': "form-control form-control-user", 'placeholder': "Строка поиска"}),
        }

