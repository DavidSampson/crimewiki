from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from crimewiki.settings import LOGIN_URL

from .models import Page, PageForm, PageTypes

def detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    if request.method == 'GET':
        context = {
            'page': page,
            'form': PageForm(instance=page)
        }
        return render(request, 'pages/detail.html', context)
    elif request.method == 'POST':
        if page.owner == request.user:
            form = PageForm(request.POST, instance=page)
            if form.is_valid():
                page = form.save(commit=False)
                page.owner = request.user
                page.save()
                return HttpResponseRedirect(f'/pages/{page_id}')
        else:
            return redirect(LOGIN_URL)

def index(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PageForm()
        context = {
            'page_list': Page.objects.all(),
            'forms': PageTypes,
            'form': PageForm() }
        return render(request, 'pages/index.html', context)

def create(request, type):
    if request.method == 'POST':
        form = PageTypes[type]['form'](request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return Http404()
