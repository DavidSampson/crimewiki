from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from pages.models import Page

class Home(ListView):
    model = Page
    template_name = 'index.html'

class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'user_form.html'
    success_url = '/'

class UserDetail(DetailView):
    model = User
