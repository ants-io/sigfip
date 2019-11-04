from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from . import mixins
from ..models import DocumentCategory
from ..forms import DocumentCategoryModelForm


class DocumentCategoryMixin(mixins.PageMixin):
    page = {
        'title': 'Organismes Payeur',
        'namespaces': {
            'create': 'app:document_categories:create',
            'update': 'app:document_categories:update',
            'delete': 'app:document_categories:delete',
            'list': 'app:document_categories:list',
        },
        'field_list': [
            {'name': 'name', 'label': 'Nom'},
            {'name': 'description', 'label': 'Description'},
            {'name': 'required_number', 'label': 'Nombre exigé'}
        ]
    }


class DocumentCategoryListView(LoginRequiredMixin, DocumentCategoryMixin, ListView):

    model = DocumentCategory
    paginate_by = 20


document_categories_list_view = DocumentCategoryListView.as_view()


class DocumentCategoryCreateView(LoginRequiredMixin, CreateView):

    model = DocumentCategory
    form_class = DocumentCategoryModelForm
    success_url = reverse_lazy('app:document_categories:list')


document_categories_create_view = DocumentCategoryCreateView.as_view()


class DocumentCategoryUpdateView(LoginRequiredMixin, UpdateView):

    model = DocumentCategory
    form_class = DocumentCategoryModelForm
    success_url = reverse_lazy('app:document_categories:list')


document_categories_update_view = DocumentCategoryUpdateView.as_view()


class DocumentCategoryDeleteView(LoginRequiredMixin, DocumentCategoryMixin, DeleteView):

    model = DocumentCategory
    success_url = reverse_lazy('app:document_categories:list')


document_categories_delete_view = DocumentCategoryDeleteView.as_view()
