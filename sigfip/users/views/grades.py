from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from . import mixins
from ..models import Grade
from ..forms import GradeModelForm


class GradeMixin(mixins.PageMixin):
    page = {
        'title': 'Grade',
        'namespaces': {
            'create': 'app:grades:create',
            'update': 'app:grades:update',
            'delete': 'app:grades:delete',
            'list': 'app:grades:list',
        },
        'field_list': [
            {'name': 'name', 'label': 'Nom'},
            {'name': 'retired_to', 'label': 'Age retraité'},
            {'name': 'corps', 'label': 'Corps'}
        ]
    }


class GradeListView(LoginRequiredMixin, GradeMixin, ListView):

    model = Grade
    paginate_by = 20


grades_list_view = GradeListView.as_view()


class GradeCreateView(LoginRequiredMixin, CreateView):

    model = Grade
    form_class = GradeModelForm
    success_url = reverse_lazy('app:grades:list')


grades_create_view = GradeCreateView.as_view()


class GradeUpdateView(LoginRequiredMixin, UpdateView):

    model = Grade
    form_class = GradeModelForm
    success_url = reverse_lazy('app:grades:list')


grades_update_view = GradeUpdateView.as_view()


class GradeDeleteView(LoginRequiredMixin, GradeMixin, DeleteView):

    model = Grade
    success_url = reverse_lazy('app:grades:list')


grades_delete_view = GradeDeleteView.as_view()
