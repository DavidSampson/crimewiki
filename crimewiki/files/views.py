import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, FileResponse

from crimewiki.settings import MEDIA_ROOT
from .forms import FileForm, AddCaseForm

from .models import File

from .utilities import map_file_to_type


def detail(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    context = {'file': file, 'cases': file.case_set.all(), 'form': AddCaseForm()}
    return render(request, 'files/detail.html', context)

def index(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.type = map_file_to_type(new_file.file_path.name)
            new_file.save()
            return HttpResponseRedirect('/')
    else:
        form = FileForm()
    context = {
        'file_list': File.objects.all(),
        'form': form}
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

def file_serve(request, file_id, file_name):
    file = get_object_or_404(File, pk=file_id)
    if file_name == file.file_path.name:
        file_route = os.path.join(MEDIA_ROOT, file_name)
        return FileResponse(open(file_route, 'rb'))
    else:
        return Http404()
