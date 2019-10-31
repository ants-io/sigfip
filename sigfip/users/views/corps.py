from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from . import mixins
from ..models import Corps
from ..forms import CorpsModelForm


class CorpMixin(mixins.PageMixin):
    page = {
        'title': 'Corps',
        'namespaces': {
            'create': 'app:corps:create',
            'update': 'app:corps:update',
            'delete': 'app:corps:delete',
            'list': 'app:corps:list',
        },
        'field_list': [
            {'name': 'name', 'label': 'Nom'},
            {'name': 'description', 'label': 'Description'}
        ]
    }


class CorpsListView(LoginRequiredMixin, CorpMixin, ListView):

    model = Corps
    paginate_by = 20


corps_list_view = CorpsListView.as_view()


class CorpsCreateView(LoginRequiredMixin, CreateView):

    model = Corps
    form_class = CorpsModelForm
    success_url = reverse_lazy('app:corps:list')


corps_create_view = CorpsCreateView.as_view()


class CorpsUpdateView(LoginRequiredMixin, UpdateView):

    model = Corps
    form_class = CorpsModelForm
    success_url = reverse_lazy('app:corps:list')


corps_update_view = CorpsUpdateView.as_view()


class CorpsDeleteView(LoginRequiredMixin, CorpMixin, DeleteView):

    model = Corps
    success_url = reverse_lazy('app:corps:list')


corps_delete_view = CorpsDeleteView.as_view()
