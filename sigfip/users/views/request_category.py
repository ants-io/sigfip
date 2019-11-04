from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from . import mixins
from ..models import RequestCategory
from ..forms import RequestCategoryModelForm


class RequestCategoryMixin(mixins.PageMixin):
    page = {
        'title': 'Organismes Payeur',
        'namespaces': {
            'create': 'app:request_categories:create',
            'update': 'app:request_categories:update',
            'delete': 'app:request_categories:delete',
            'list': 'app:request_categories:list',
        },
        'field_list': [
            {'name': 'name', 'label': 'Nom'},
            {'name': 'description', 'label': 'Description'}
        ]
    }


class RequestCategoryListView(LoginRequiredMixin, RequestCategoryMixin, ListView):

    model = RequestCategory
    paginate_by = 20


request_categories_list_view = RequestCategoryListView.as_view()


class RequestCategoryCreateView(LoginRequiredMixin, CreateView):

    model = RequestCategory
    form_class = RequestCategoryModelForm
    success_url = reverse_lazy('app:request_categories:list')


request_categories_create_view = RequestCategoryCreateView.as_view()


class RequestCategoryUpdateView(LoginRequiredMixin, UpdateView):

    model = RequestCategory
    form_class = RequestCategoryModelForm
    success_url = reverse_lazy('app:request_categories:list')


request_categories_update_view = RequestCategoryUpdateView.as_view()


class RequestCategoryDeleteView(LoginRequiredMixin, RequestCategoryMixin, DeleteView):

    model = RequestCategory
    success_url = reverse_lazy('app:request_categories:list')


request_categories_delete_view = RequestCategoryDeleteView.as_view()
