from django.shortcuts import render
from files.models import File
from pages.models import Page
# Create your views here.

def index(request):
    context = {
        'file_list': File.objects.all(),
        'page_list': Page.objects.all(),
    }
    return render(request, 'index.html', context)
