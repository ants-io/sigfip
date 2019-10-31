from django import template

from django.urls import reverse_lazy


register = template.Library()


def get_url(namespace, **kwargs):
    return reverse_lazy(namespace, kwargs={kwargs})


# register.simple_tag('get_url', get_url)
