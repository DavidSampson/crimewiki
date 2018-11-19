from django.shortcuts import render, get_object_or_404
from django.http.response import Http404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from files.models import File
from cases.models import Case
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form':form})
    else:
        return Http404()

def index(request):
    pass

def detail(request, user_id):
    context = {
        'user_detail': get_object_or_404(User, pk=user_id),
        'file_list': File.objects.filter(owner=user_id),
        'case_list': Case.objects.filter(owner=user_id)
    }
    return render(request, 'users/detail.html', context)
