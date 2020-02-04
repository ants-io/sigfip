import datetime
import math
from datetime import timedelta

from django.db.models.functions import ExtractMonth
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status as status_code

from .. import models, forms
from . import serializers
from ..views.api import serializers as srv2

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = srv2.UserSerializer


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = models.Salary.objects.all()
    serializer_class = serializers.SalarySerializer


class CorpsViewSet(viewsets.ModelViewSet):
    queryset = models.Corps.objects.all()
    serializer_class = serializers.CorpsSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = models.Profession.objects.all()
    serializer_class = serializers.ProfessionSerializer


class MinistryViewSet(viewsets.ModelViewSet):
    queryset = models.Ministry.objects.all()
    serializer_class = serializers.MinistrySerializer


class PayingOrgViewSet(viewsets.ModelViewSet):
    queryset = models.PayingOrg.objects.all()
    serializer_class = serializers.PayingOrgSerializer


class DocumentCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.DocumentCategory.objects.all()
    serializer_class = serializers.DocumentCategory


class RequestCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.RequestCategory.objects.all()
    serializer_class = serializers.RequestCategorySerializer


class SlipViewSet(viewsets.ModelViewSet):
    queryset = models.Slip.objects.all()
    serializer_class = serializers.SlipSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = models.Request.objects.all()
    serializer_class = srv2.LoanSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if not data['documents']:
            return Response(
                {
                    "error": {
                        "message": f"Veuillez saisir les documents requis.",
                        "code": 400,
                    }
                },
                status=status_code.HTTP_400_BAD_REQUEST)

        try:
            line = models.PrepaymentTable.objects.get(
                loan_amount=data['amount_requested'])
        except models.PrepaymentTable.DoesNotExist:
            return Response(
                {
                    "error": {
                        "message":
                        f"Le montant {data['amount_requested']} n'est pas pris en comte.",
                        "code": 400,
                    }
                },
                status=status_code.HTTP_400_BAD_REQUEST)

        user = models.User.objects.get(pk=data['user'])
        if user.salary < line.minimal_salary:
            return Response(
                {
                    "error": {
                        "message":
                        f"Le salaire minimal authorisé pour ce prêt est de {line.minimal_salary} F CFA.",
                        "code": 400,
                    }
                },
                status=status_code.HTTP_400_BAD_REQUEST)

        form = forms.LoanForm(data)
        document_ids = []
        provided_numbers = []
        references = []
        document_dates = []

        if form.is_valid():
            model = form.save(commit=False)

            if not model.monthly_payment_number:
                model.monthly_payment_number = line.duration * 12

            model.amount_awarded = model.amount_requested
            model.amount_to_repay = model.amount_awarded
            model.quota = model.user.salary / 3
            model.withholding = math.ceil(model.amount_awarded /
                                          model.monthly_payment_number)
            # model.treatment_agent_id = data['treatment_agent']
            model.save()

            for document in data['documents']:
                doc_form = forms.DocumentForm({
                    'request':
                    model.id,
                    'document_category':
                    document['id'],
                    'provided_number':
                    document['provided_number'],
                    'reference':
                    document['reference'],
                    'document_date':
                    document['document_date']
                    if 'document_date' in document else None
                })

                # Handle when it's false.
                if doc_form.is_valid():
                    doc_form.save()
        else:
            return Response(
                {
                    "error": {
                        "errors": form.errors,
                        "message":
                        f"Erreur dans les informations saisie, veuillez saisir les informations.",
                        "code": 400,
                    }
                },
                status=status_code.HTTP_400_BAD_REQUEST)

        return Response(srv2.LoanSerializer(model, many=False).data)

    @action(detail=False)
    def extract_by_period(self, request, *args, **kwargs):
        start_at = request.GET.get('start_at')
        end_at = request.GET.get('end_at')

        if start_at:
            start_at = datetime.datetime.strptime(start_at, "%Y-%m-%d").date()
        else:
            start_at = datetime.date.today() - timedelta(days=31)

        if end_at:
            end_at = datetime.datetime.strptime(end_at, "%Y-%m-%d").date()
        else:
            end_at = datetime.date.today()

        loans = models.Request.objects.filter(
            created_at__range=[start_at, end_at])

        serialized_loans = srv2.ExtraSmallLoanSerializer(loans, many=True)

        return Response(serialized_loans.data)

    @action(detail=False)
    def queue(self, request, *args, **kwargs):
        size = request.GET.get('size', '20')
        users = models.User.objects.filter(request__status='pending').distinct(
        ).order_by('request__submit_date')
        serialized_users = srv2.ExtraSmallUserSerializer(users, many=True)
        return Response(serialized_users.data)
