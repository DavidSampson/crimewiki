from django.forms import ModelForm
from django import forms
from .models import File
class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['file_path', 'name', 'description', 'source']
