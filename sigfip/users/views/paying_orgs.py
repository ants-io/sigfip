from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from . import mixins
from ..models import PayingOrg
from ..forms import PayingOrgModelForm


class PayingOrgMixin(mixins.PageMixin):
    page = {
        'title': 'Organismes Payeur',
        'namespaces': {
            'create': 'app:paying_orgs:create',
            'update': 'app:paying_orgs:update',
            'delete': 'app:paying_orgs:delete',
            'list': 'app:paying_orgs:list',
        },
        'field_list': [
            {'name': 'name', 'label': 'Nom'},
            {'name': 'description', 'label': 'Description'}
        ]
    }


class PayingOrgListView(LoginRequiredMixin, PayingOrgMixin, ListView):

    model = PayingOrg
    paginate_by = 20


paying_orgs_list_view = PayingOrgListView.as_view()


class PayingOrgCreateView(LoginRequiredMixin, CreateView):

    model = PayingOrg
    form_class = PayingOrgModelForm
    success_url = reverse_lazy('app:paying_orgs:list')


paying_orgs_create_view = PayingOrgCreateView.as_view()


class PayingOrgUpdateView(LoginRequiredMixin, UpdateView):

    model = PayingOrg
    form_class = PayingOrgModelForm
    success_url = reverse_lazy('app:paying_orgs:list')


paying_orgs_update_view = PayingOrgUpdateView.as_view()


class PayingOrgDeleteView(LoginRequiredMixin, PayingOrgMixin, DeleteView):

    model = PayingOrg
    success_url = reverse_lazy('app:paying_orgs:list')


paying_orgs_delete_view = PayingOrgDeleteView.as_view()
