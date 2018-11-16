from django.db import models

from files.models import File
# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length = 200)
    files = models.ManyToManyField(File)
    def __str__(self):
        return self.name