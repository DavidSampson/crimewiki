from django.views.generic import ListView
from pages.models import Page

class Home(ListView):
    model = Page
    template_name = 'index.html'
