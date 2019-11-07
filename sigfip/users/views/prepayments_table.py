from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from . import mixins
from ..models import PrepaymentTable
from ..forms import PrepaymentTableForm


class PrepaymentTableMixin(mixins.PageMixin):
    page = {
        'title': 'Table des précomptes',
        'namespaces': {
            'create': 'app:prepayments_table:create',
            'update': 'app:prepayments_table:update',
            'delete': 'app:prepayments_table:delete',
            'list': 'app:prepayments_table:list',
        },
        'field_list': [
            {'name': 'loan_amount', 'label': 'Montant du prêt'},
            {'name': 'duration', 'label': 'Durée (année)'},
            {'name': 'monthly_withdrawal', 'label': 'Prélévement mensuel'},
            {'name': 'recoverable_third_party', 'label': 'Tiers saisissable'},
            {'name': 'minimal_salary', 'label': 'Salaire minimum'}
        ]
    }


class PrepaymentTableListView(LoginRequiredMixin, PrepaymentTableMixin, ListView):

    model = PrepaymentTable
    paginate_by = 20


prepayments_table_list_view = PrepaymentTableListView.as_view()


class PrepaymentTableCreateView(LoginRequiredMixin, CreateView):

    model = PrepaymentTable
    form_class = PrepaymentTableForm
    success_url = reverse_lazy('app:prepayments_table:list')


prepayments_table_create_view = PrepaymentTableCreateView.as_view()


class PrepaymentTableUpdateView(LoginRequiredMixin, UpdateView):

    model = PrepaymentTable
    form_class = PrepaymentTableForm
    success_url = reverse_lazy('app:prepayments_table:list')


prepayments_table_update_view = PrepaymentTableUpdateView.as_view()


class PrepaymentTableDeleteView(LoginRequiredMixin, PrepaymentTableMixin, DeleteView):

    model = PrepaymentTable
    success_url = reverse_lazy('app:prepayments_table:list')


prepayments_table_delete_view = PrepaymentTableDeleteView.as_view()
