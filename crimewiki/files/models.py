from django.db import models
from django.contrib.auth.models import User
from .utilities import file_types

class File(models.Model):
    file_path = models.FileField()
    type = models.CharField(max_length=10, choices=file_types, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    def __str__(self):
        return self.file_path.name
