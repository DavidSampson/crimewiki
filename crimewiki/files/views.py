from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404

from .forms import FileForm, AddCaseForm

from .models import File

from cases.models import Case

def detail(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    return render(request, 'files/detail.html', {'file': file, 'cases': file.case_set.all(), 'form': AddCaseForm()})

def index(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FileForm()
    context = { 
        'file_list': File.objects.all(),
        'form': form }
    return render(request, 'files/index.html', context)

def add_cases(request, file_id):
    if request.method == 'POST':
        file = get_object_or_404(File, pk=file_id)
        form = AddCaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for case in data['cases']:
                case.files.add(file)
                case.save()
            return HttpResponseRedirect(f'/files/{file_id}')
    else:
        return Http404()
