from django.contrib import messages
from django.http import HttpResponse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from .. import forms, models


class PageMixin(object):
    page = {'title': '', 'namespaces': {}, 'field_list': []}

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
        return {'loan_form': forms.LoanForm()}

    def post(self, request, *args, **kwargs):

        if 'update_loan' in request.POST:
            form = forms.LoanDetailForm(request.POST,
                                        instance=self.get_object())

        if 'add_load' in request.POST:
            form = forms.LoanForm(request.POST)

        print(form.errors)

        document_ids = []
        provided_numbers = []
        references = []
        document_dates = []

        # TODO: handle when it's not the case.
        if form.is_valid():
            model = form.save(commit=False)

            messages.add_message(request, messages.SUCCESS,
                                 _("INFO: La demande a bien été ajoutée."))

            if not model.monthly_payment_number:
                line = models.PrepaymentTable.objects.get(
                    loan_amount=model.amount_requested)
                if model.user.salary < line.minimal_salary:
                    messages.add_message(
                        request, messages.ERROR,
                        _("INFO: Le salaire minimal authorisé pour ce prêt est de {line.minimal_salary} F CFA."
                          ))
                    return self.get(request, *args, **kwargs)

                # TODO: This treatment has to be done every time we trying to save object state.
                model.monthly_payment_number = line.duration * 12

            model.amount_awarded = model.amount_requested
            model.amount_to_repay = model.amount_awarded
            model.quota = model.user.salary / 3
            model.withholding = model.amount_awarded / model.monthly_payment_number
            model.treatment_agent_id = request.user.id
            model.save()

        document_ids = request.POST.getlist('document_id')
        provided_numbers = request.POST.getlist('provided_number')
        references = request.POST.getlist('reference')
        document_dates = request.POST.getlist('document_date')

        if 'add_load' in request.POST:
            for document_id, provided_number, reference, document_date in zip(
                    document_ids, provided_numbers, references,
                    document_dates):
                doc_form = forms.DocumentForm({
                    'request': model.id,
                    'document_category': document_id,
                    'provided_number': provided_number,
                    'reference': reference,
                    'document_date': document_date
                })

                # Handle when it's false.
                if doc_form.is_valid():
                    doc_form.save()

        if 'update_loan' in request.POST:
            for document_id, provided_number, reference, document_date in zip(
                    document_ids, provided_numbers, references,
                    document_dates):
                doc = models.Document.objects.get(pk=document_id)
                doc.provided_number = provided_number
                doc.reference = reference
                doc.document_date = document_date
                doc.save()

        return self.get(request, *args, **kwargs)


class LoanDetailMixin(object):
    @cached_property
    def forms(self):
        return {'form': forms.LoanDetailForm(instance=self.get_object())}
