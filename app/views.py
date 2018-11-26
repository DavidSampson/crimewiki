from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Page, PageTypes, File
from .utilities import map_file_to_type
from .mixins import LoginRequiredForEditMixin

class Home(ListView):
    model = Page
    template_name = 'index.html'

class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'users/user_form.html'
    redirect_url = '/'

class UserDetail(DetailView):
    model = User

class PageMixin(LoginRequiredForEditMixin):
    queryset = Page.objects.select_subclasses()
    def form_valid(self, form):
        form.instance.owner = self.request.user
        if self.get_form_class() == File:
            form.instance.type = map_file_to_type(form.instance.file_path.name)
        return super().form_valid(form)

class PageDetail(PageMixin, UpdateView):
    extra_context = {'map_api_key': settings.MAP_API_KEY}
    template_name_suffix = '_detail'
    def get_form_class(self):
        return PageTypes[type(self.object).__name__]["form"]

class PageIndex(PageMixin, ListView):
    template_name = 'pages/page_list.html'
    extra_context = {'forms': PageTypes}

class PageCreate(CreateView):
    def get_form_class(self):
        return PageTypes[self.kwargs.get('type')]['form']
