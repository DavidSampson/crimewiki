from django.conf import settings
from django.views.generic import ListView, CreateView, UpdateView


from pages.models import Page, PageTypes
from pages.utilities import map_file_to_type
from pages.mixins import MethodPermissionRequiredMixin


class PageMixin(MethodPermissionRequiredMixin):
    queryset = Page.objects.select_subclasses()

    def form_valid(self, form):
        form.instance.owner = self.request.user
        if form.instance.file_path:
            form.instance.type = map_file_to_type(form.instance.file_path.name)
        return super().form_valid(form)


class PageDetail(PageMixin, UpdateView):
    required_permissions = {'post': 'change_page'}
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
