from django.contrib import messages
from django.http import HttpResponse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from .. import forms


class PageMixin(object):
    page = {
        'title': '',
        'namespaces': {},
        'field_list': []
    }

    def get_page(self):
        return self.page

    def get_page_title(self):
        return self.page['title']

    def get_namespaces(self):
        return self.page['namespaces']

    def get_page_field_list(self):
        return self.page['field_list']

    def get_context_data(self, **kwargs):
        context = super(PageMixin, self).get_context_data(**kwargs)

        context.update({
            'page': {
                'title': self.get_page_title(),
                'namespaces': self.get_namespaces(),
                'field_list': self.get_page_field_list()
            },
        })

        return context


class UserDetailMixin(object):

    @cached_property
    def forms(self):
        return {
            'loan_form': forms.LoanForm()
        }

    def post(self, request, *args, **kwargs):

        if 'add_load' in request.POST:
            form = forms.LoanForm(request.POST)
            document_ids = []
            provided_number = []
            references = []
            document_dates = []

            # TODO: handle when it's not the case.
            if form.is_valid():
                model = form.save()

                document_ids = request.POST.getlist('document_id')
                provided_numbers = request.POST.getlist('provided_number')
                references = request.POST.getlist('reference')
                document_dates = request.POST.getlist('document_date')

            for document_id, provided_number, reference, document_date in zip(
                    document_ids,
                    provided_numbers,
                    references,
                    document_dates):
                doc_form = forms.DocumentForm({
                    'request': model.id,
                    'document_category': document_id,
                    'provided_number': provided_number,
                    'reference': reference,
                    # 'document_date': document_date, Add later.
                })

                # Handle when it's false.
                if doc_form.is_valid():
                    doc_form.save()

            messages.add_message(
                request, messages.INFO, _("INFO: La demande a bien été ajoutée.")
            )

        return self.get(request, *args, **kwargs)
