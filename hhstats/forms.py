from django import forms
from hhrequest.models import Requests

# класс для определения формы для запроса по статистике региона
class StatsRequestsForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields =('region',)
        widgets = {
            'region': forms.TextInput(attrs={'class': "form-control form-control-user", 'placeholder':'Регион'}),
        }
