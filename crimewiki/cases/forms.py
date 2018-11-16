from django.forms import ModelForm
from .models import Case

class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ['name', 'files']
