from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import CaseForm

from .models import Case

def detail(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'GET':
        context = {'case': case, 'files': case.files.all(), 'form': CaseForm(instance=case)}
        return render(request, 'cases/detail.html', context)
    elif request.method == 'POST':
        form = CaseForm(request.POST, request.FILES, instance=case)
        if form.is_valid():
            case = form.save(commit=False)
            case.owner = request.user
            case.save()
            return HttpResponseRedirect(f'/cases/{case_id}')

def index(request):
    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CaseForm()
    context = {
        'case_list': Case.objects.all(),
        'form': form }
    return render(request, 'cases/index.html', context)
