from django.db.models import Q

from .builder import QueryBuilder


class QQueryBuilder(QueryBuilder):

    _prefix = None
    _q = ''
    _operator = 'icontains'
    _params = []
    _queries = None

    def __init__(self, **kwargs):
        self._prefix = 'user' \
            if kwargs.get('prefix') \
            else None
        self._params = kwargs.get('params')
        self._q = kwargs.get('query')

        operator = kwargs.get('operator')
        if operator:
            self._operator = operator

    def build(self):
        if not self._params:
            raise ValueError("No params initialized")

        if not self._q:
            return
        query = Q()
        for attr in self._params:
            key = f'{attr}__{self._operator}' \
                if not self._prefix \
                else f'{self._prefix}__{attr}__{self._operator}'

            q = {key: self._q}
            query |= Q(**q)

        self._queries = query

    def get_result(self):
        return self._queries
