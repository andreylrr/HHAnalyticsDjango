from django import forms
from hhrequest.models import Requests

class StatsRequestsForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields =('region',)
        widgets = {
            'region': forms.TextInput(attrs={'class': "form-control form-control-user", 'placeholder':'Регион'}),
        }
