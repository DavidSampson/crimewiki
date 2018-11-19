from django.db import models
from django.contrib.auth.models import User
from files.models import File
# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    files = models.ManyToManyField(File, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    def __str__(self):
        return self.name
