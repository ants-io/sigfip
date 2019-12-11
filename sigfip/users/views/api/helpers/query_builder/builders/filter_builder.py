from .builder import QueryBuilder


class FilterParam:
    prefix = False
    name = ''
    op = ''
    value = ''

    def __init__(self, **kwargs):
        self.prefix = kwargs.get('prefix')
        self.name = kwargs.get('name')
        self.op = kwargs.get('op')
        self.value = kwargs.get('value')

    @property
    def kind(self):
        if 'after' in self.name:
            return 'date'
        elif 'Ids' in self.name:
            return

    @property
    def key(self):
        return f'{self.name}__{self.op}' \
            if not self.prefix \
            else f'{self.prefix}__{self.name}__{self.op}'

    def get_query(self):
        return {self.key: self.value}


class FilterQueryBuilder(QueryBuilder):

    def __init__(self, **kwargs):
        pass
