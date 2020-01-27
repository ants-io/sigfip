from enum import Enum

from django.db.models import Q
from django.db.models.functions import ExtractYear
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ... import models
from . import serializers
from .helpers.query_builder.director import QueryDirector


class SearchEnum(Enum):
    PerAgent = "0"
    PerLoan = "1"


@api_view(['POST'])
def searching(request):
    params = request.data
    search_by_loans = request.data[
        'searchCategory'] == SearchEnum.PerLoan.value
    model = models.Request \
        if search_by_loans\
        else models.User
    serializer = serializers.LoanSerializer \
        if search_by_loans \
        else serializers.UserSerializer

    director = QueryDirector(option='QQUERY', params=params, model=model)
    q_query = director.make()
    results = []

    if not search_by_loans:
        results = model.objects.annotate(age=timezone.now().year -
                                         ExtractYear('birth_date__year'))
    else:
        results = model.objects.annotate(age=timezone.now().year -
                                         ExtractYear('user__birth_date__year'))

    if q_query:
        results = results.filter(q_query)
    # end

    director = QueryDirector(params=params, model=model)
    f_query = director.make()

    if f_query:
        results = results.filter(**f_query)

    serialized_data = serializer(results, many=True)

    return Response({
        'search_type': 'loans' if search_by_loans else 'users',
        'data': serialized_data.data
    })
