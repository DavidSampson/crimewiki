from django.db import models
from django.contrib.auth.models import User
from pages.models import Page
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
