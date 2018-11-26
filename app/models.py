from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import modelform_factory
from model_utils.managers import InheritanceManager
from .utilities import file_types

class Page(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    objects = InheritanceManager()
    def get_absolute_url(self):
        return reverse('pages:detail', args=[str(self.id)])
    def __str__(self):
        return self.name
    def get_excluded_fields(self):
        return ['owner']

class Entry(Page):
    content = models.TextField()

class File(Page):
    type = models.CharField(max_length=10, choices=file_types, blank=True)
    source = models.CharField(max_length=200, blank=True)
    file_path = models.FileField()
    def get_excluded_fields(self):
        fields = super().get_excluded_fields()
        fields.append('type')
        return fields

class Location(Page):
    place = models.CharField(max_length=200)


PageTypesList = [Entry, File, Location]

PageTypes = {
    t.__name__: {'model': t, 'form': modelform_factory(t, exclude=t().get_excluded_fields())}
    for t in PageTypesList
    }
