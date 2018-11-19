from django.forms import ModelForm
from django import forms
from cases.models import Case
from .models import File
class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['file_path', 'name', 'description', 'source']

class AddCaseForm(forms.Form):
    cases = forms.ModelMultipleChoiceField(queryset=Case.objects.all(), label="Select cases to add")
    