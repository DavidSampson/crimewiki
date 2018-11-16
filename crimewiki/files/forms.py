from django.forms import ModelForm
from django import forms
from .models import File
from cases.models import Case
class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['file_path']

class AddCaseForm(forms.Form):
    cases = forms.ModelMultipleChoiceField(queryset=Case.objects.all(), label="Select cases to add")