import datetime
from datetime import timedelta

from django.db.models.functions import ExtractMonth
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response

from .. import models
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


class RequestViewSet(viewsets.ModelViewSet):
    queryset = models.Request.objects.all()
    serializer_class = srv2.LoanSerializer

    @action(detail=False)
    def extract_by_period(self, request, *args, **kwargs):
        start_at = request.GET.get('start_at')
        end_at = request.GET.get('end_at')
        extract_by = request.GET.get('extract_by')
        delta_day = timedelta(days=1)

        if start_at:
            start_at = datetime.datetime.strptime(
                start_at, "%Y-%m-%d").date() - delta_day
        else:
            start_at = datetime.date.today() - timedelta(days=31)

        if end_at:
            end_at = datetime.datetime.strptime(end_at,
                                                "%Y-%m-%d").date() + delta_day
        else:
            end_at = datetime.date.today() + delta_day

        if extract_by == 'submit_data':
            loans = models.Request.objects.filter(
                submit_date__range=[start_at, end_at])

        if extract_by == 'proceed_data':
            loans = models.Request.objects.filter(
                proceed_date__range=[start_at, end_at])

        data = []
        serialized_loans = srv2.ExtraSmallLoanSerializer(loans, many=True)
        for d in serialized_loans.data:
            d.update({"type": extract_by})
            data.append(d)
        return Response(data)

    @action(detail=False)
    def recap(self, request, *args, **kwargs):
        today = datetime.date.today()
        year = request.GET.get('year') if request.GET.get(
            'year') else today.year
        fields = ['submit_date', 'proceed_date']
        months_data = {
            "1": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "2": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "3": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "4": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "5": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "6": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "7": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "8": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "9": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "10": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "11": {
                'submit_date': 0,
                'proceed_date': 0
            },
            "12": {
                'submit_date': 0,
                'proceed_date': 0
            },
        }
        for field in fields:
            year_filter = {f'{field}__year': year}
            data = models.Request.objects\
                .filter(**year_filter)\
                .annotate(month=ExtractMonth(f'{field}__month'))\
                .values('month').annotate(c=Count('id'))\
                .order_by()
            for d in data:
                months_data[str(d['month'])].update({field: d['c']})

        return Response(months_data)