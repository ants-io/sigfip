from django.test import TestCase

from ..... import models
from .....views.api.helpers.query_builder.director import QueryDirector


class TestDirector(TestCase):

    def setUp(self):
        self.params = {
            'age_after': 45,
            'age_before': 20,
            'branchIds': [2, 1],
            'category': 0,
            'convention': "",
            'dateIntervals': "",
            'gradeIds': [2, 1],
            'ministryIds': [],
            'payingOrgIds': [],
            'post_reference': "",
            'proceed_date_after': "",
            'proceed_date_before': "",
            'professionsIds': [2, 1],
            'query': "gueye",
            'searchCategory': "0",
            'status': [],
            'submit_date_after': "",
            'submit_date_before': "",
        }
        self.model = models.Request
        self.director = QueryDirector(
            params=self.params,
            model=self.model
        )

    def test_make(self):
        self.assertIsNotNone(self.director.make())
