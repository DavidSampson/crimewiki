from django.db import models
from django.contrib.auth.models import User
from .utilities import file_types
from django.forms import ModelForm, modelform_factory

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    def __str__(self):
        return self.name

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

class Entry(Page):
    content = models.TextField()

class File(Page):
    type = models.CharField(max_length=10, choices=file_types, blank=True)
    file_path = models.FileField()

PageTypesList = [Entry, File]

PageTypes = {t.__name__: {'model': t, 'form': modelform_factory(t, fields='__all__')} for t in PageTypesList }
