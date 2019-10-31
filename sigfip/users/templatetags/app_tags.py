from django import template

from django.urls import reverse_lazy


register = template.Library()


@register.simple_tag
def get_attr(object, attr):
    return getattr(object, attr)
