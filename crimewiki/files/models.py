from django.db import models
from .utilities import file_types

class File(models.Model):
    file_path = models.FileField()
    type = models.CharField(max_length=10,choices=file_types, blank=True)
    def __str__(self):
        return self.file_path.name
