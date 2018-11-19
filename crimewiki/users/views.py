from django.shortcuts import render, get_object_or_404
from django.http.response import Http404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    user_detail = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'user_detail':user_detail})
