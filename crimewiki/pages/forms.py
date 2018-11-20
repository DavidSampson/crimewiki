from django.forms import ModelForm
from .models import Page, PageTypes

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = '__ALL__'

def Former(Types):
    _ = {}
    for Type in Types:
        class Form(PageForm):
            class Meta:
                model = Type
                fields = '__ALL__'
        _[Type.__name__] = Form
    return _

Forms = Former(PageTypes)
