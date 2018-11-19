from django.db import models
from django.contrib.auth.models import User
from .utilities import file_types

class File(models.Model):
    file_path = models.FileField()
    name = models.CharField(max_length=256, blank=True)
    type = models.CharField(max_length=10, choices=file_types, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    description = models.TextField(blank=True)
    source = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.file_path.name
