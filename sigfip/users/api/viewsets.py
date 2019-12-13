from ..models import User
from .serializers import *

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class CorpsViewSet(viewsets.ModelViewSet):
    queryset = Corps.objects.all()
    serializer_class = CorpsSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer


class PayingOrgViewSet(viewsets.ModelViewSet):
    queryset = PayingOrg.objects.all()
    serializer_class = PayingOrgSerializer


class DocumentCategoryViewSet(viewsets.ModelViewSet):
    queryset = DocumentCategory.objects.all()
    serializer_class = DocumentCategory


class RequestCategoryViewSet(viewsets.ModelViewSet):
    queryset = RequestCategory.objects.all()
    serializer_class = RequestCategorySerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
