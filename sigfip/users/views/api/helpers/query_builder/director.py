from ..... import models
from .builders.q_query import QQueryBuilder
from .builders.filter_builder import FilterQueryBuilder


class QueryDirector:

    _params = None
    _model = None
    _option = 'QQUERY'

    def __init__(self, **kwargs):
        self._model = models.Request \
            if models.Request == kwargs.get('model') \
            else models.User
        self._params = kwargs.get('params')
        self._option = kwargs.get('option')

    def make(self):
        if self._option == 'QQUERY':
            return self.make_q_query()
        else:
            return self.make_filter_query()

    def make_q_query(self):
        q_query_builder = QQueryBuilder(
            prefix=self._model == models.Request,
            query=self._params['query'],
            params=[
                'first_name',
                'last_name',
                'cni',
                'registration_number',
                'address',
                'phone',
                'grade__name',
                'ministry__name',
                'paying_org__name',
            ])
        q_query_builder.build()
        return q_query_builder.get_result()

    def make_filter_query(self):
        filter_query = {}

        if 'age' in self._params:
            filter_query.update({
                'age__gte': self._params['age_after'],
                'age__lte': self._params['age_before']
            })
        if 'branchIds' in self._params:
            filter_query.update({
                'grade__corps_id__in': self._params['branchIds']
            })
        if 'gradeIds' in self._params:
            filter_query.update({
                'grade_id__in': self._params['gradeIds']
            })
        if 'ministryIds' in self._params:
            filter_query.update({
                'ministry_id__in': self._params['ministryIds']
            })
        if 'payingOrgIds' in self._params:
            filter_query.update({
                'paying_org_id__in': self._params['payingOrgIds']
            })
        if 'professionsIds' in self._params:
            filter_query.update({
                'profession_id__in': self._params['professionsIds']
            })

        if self._model == models.Request:
            if 'proceed_date_before' in self._params:
                filter_query.update({
                    'proceed_date_after__gte': self._params['age_after'],
                    'proceed_date_before__lte': self._params['proceed_date_before']
                })
            if 'submit_date_after' in self._params:
                filter_query.update({
                    'submit_date_after__gte': self._params['submit_date_after'],
                    'submit_date_before__lte': self._params['submit_date_before']
                })
            if 'convention' in self._params:
                filter_query.update({
                    'convention__icontains': self._params['convention']
                })
            if 'post_reference' in self._params:
                filter_query.update({
                    'post_reference__icontains': self._params['post_reference']
                })

            filter_query = {f'user__{k}': filter_query[k] for k in filter_query.keys()}

        return filter_query
