from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Page, PageTypes, File
from .utilities import map_file_to_type
from .mixins import LoginRequiredForEditMixin

class PageMixin(LoginRequiredForEditMixin):
    queryset = Page.objects.select_subclasses()
    def form_valid(self, form):
        form.instance.owner = self.request.user
        if form.instance.file_path:
            form.instance.type = map_file_to_type(form.instance.file_path.name)
        return super().form_valid(form)

class PageDetail(PageMixin, UpdateView):
    template_name_suffix = '_detail'
    extra_context = {'map_api_key': settings.MAP_API_KEY}
    def get_form_class(self):
        return PageTypes[type(self.object).__name__]["form"]

class PageIndex(PageMixin, ListView):
    template_name = 'page_list.html'
    extra_context = {'forms': PageTypes}

class PageCreate(CreateView):
    def get_form_class(self):
        return PageTypes[self.kwargs.get('type')]['form']
