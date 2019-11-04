from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from . import mixins
from ..models import Ministry
from ..forms import MinistryModelForm


class MinistryMixin(mixins.PageMixin):
    page = {
        'title': 'Ministry',
        'namespaces': {
            'create': 'app:ministers:create',
            'update': 'app:ministers:update',
            'delete': 'app:ministers:delete',
            'list': 'app:ministers:list',
        },
        'field_list': [
            {'name': 'name', 'label': 'Nom'},
            {'name': 'description', 'label': 'Description'}
        ]
    }


class MinistryListView(LoginRequiredMixin, MinistryMixin, ListView):

    model = Ministry
    paginate_by = 20


ministers_list_view = MinistryListView.as_view()


class MinistryCreateView(LoginRequiredMixin, CreateView):

    model = Ministry
    form_class = MinistryModelForm
    success_url = reverse_lazy('app:ministers:list')


ministers_create_view = MinistryCreateView.as_view()


class MinistryUpdateView(LoginRequiredMixin, UpdateView):

    model = Ministry
    form_class = MinistryModelForm
    success_url = reverse_lazy('app:ministers:list')


ministers_update_view = MinistryUpdateView.as_view()


class MinistryDeleteView(LoginRequiredMixin, MinistryMixin, DeleteView):

    model = Ministry
    success_url = reverse_lazy('app:ministers:list')


ministers_delete_view = MinistryDeleteView.as_view()
