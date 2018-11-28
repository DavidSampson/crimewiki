from django.db import models
from django.urls import reverse
from django.forms import modelform_factory
from model_utils.managers import InheritanceManager
from pages.utilities import file_types
from crimewiki.mixins import PermissionedObjectMixin


class Page(PermissionedObjectMixin, models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    objects = InheritanceManager()

    def get_absolute_url(self):
        return reverse('page_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Entry(Page):
    content = models.TextField()


class FileCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WebResource(Page):
    link = models.URLField(max_length=200)


class File(Page):
    type = models.CharField(max_length=10, choices=file_types, blank=True)
    source = models.CharField(max_length=200, blank=True)
    file_path = models.FileField()
    category = models.ForeignKey(
        FileCategory, on_delete=models.CASCADE, null=True, blank=True)

    def get_excluded_fields(self):
        fields = super().get_excluded_fields()
        fields.append('type')
        fields.append('category')
        return fields


class FileCollection(Page):
    files = models.ManyToManyField(File)


class Location(Page):
    place = models.CharField(max_length=200)


PageTypesList = [Entry, File, Location, FileCollection, WebResource]

PageTypes = {
    t.__name__: {'model': t, 'form': modelform_factory(
        t, exclude=t().get_excluded_fields())}
    for t in PageTypesList
}
