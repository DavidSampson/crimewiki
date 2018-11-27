from django import template

register = template.Library()

@register.filter(name='strip_protocol')
def strip_protocol(val):
    return val.split('://')[-1]
