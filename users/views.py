from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView
from django.http import HttpResponseRedirect
# Create your views here.


class UserList(ListView):
    template_name = 'users/user_list.html'
    model = User


class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'user_form.html'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.groups.add('RegularUsers')
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UserDetail(DetailView):
    model = User
    template_name = 'users/user_detail.html'
