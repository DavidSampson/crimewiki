from django.db import models

class File(models.Model):
    file_path = models.FileField()
    def __str__(self):
        return self.file_path.name