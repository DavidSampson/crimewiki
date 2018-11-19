from django.shortcuts import render
from files.models import File
from cases.models import Case
# Create your views here.

def index(request):
    context = {
        'file_list': File.objects.all(),
        'case_list': Case.objects.all(),
    }
    return render(request, 'index.html', context)
    