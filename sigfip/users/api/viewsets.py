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
        # extract_by = request.GET.get('extract_by')
        # delta_day = timedelta(days=1)

        if start_at:
            start_at = datetime.datetime.strptime(start_at, "%Y-%m-%d").date()
        else:
            start_at = datetime.date.today() - timedelta(days=31)

        if end_at:
            end_at = datetime.datetime.strptime(end_at, "%Y-%m-%d").date()
        else:
            end_at = datetime.date.today()

        # if extract_by == 'submit_data':
        #     loans = models.Request.objects.filter(
        #         submit_date__range=[start_at, end_at])

        # if extract_by == 'proceed_data':
        #     loans = models.Request.objects.filter(
        #         proceed_date__range=[start_at, end_at])

        loans = models.Request.objects.filter(
            created_at__range=[start_at, end_at])

        serialized_loans = srv2.ExtraSmallLoanSerializer(loans, many=True)

        return Response(serialized_loans.data)
