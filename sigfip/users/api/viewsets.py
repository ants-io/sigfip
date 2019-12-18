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
