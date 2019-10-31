class PageMixin(object):
    page = {
        'title': '',
        'namespaces': {},
        'field_list': []
    }

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
