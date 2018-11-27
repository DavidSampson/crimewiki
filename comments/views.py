from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin
from django.forms.models import modelform_factory
from comments.models import Comment
from pages.models import Page
# Create your views here.

class Serve(FormMixin, ListView):
    template_name = 'comments/commentblock.html'
    model = Comment
    fields = ['text']
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = self.get_page()
        context["form"] = self.get_form()
        return context
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        return kwargs
    def get_success_url(self):
        return f'/pages/{self.get_page()}'
    def get_page(self):
        return self.kwargs.get('pk')
    def get_queryset(self):
        return Comment.objects.filter(page=self.get_page()).order_by('creation_date')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.page = Page.objects.get(id=self.get_page())
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
