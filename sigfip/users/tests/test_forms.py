# -*- coding: utf-8 -*-

from django.test import TestCase

import pytest

from sigfip.users.forms import (
    UserCreationForm,
    SalaryModelForm,
    CorpsModelForm
)
from sigfip.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserCreationForm:
    def test_clean_username(self):
        # A user with proto_user params does not exist yet.
        proto_user = UserFactory.build()

        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user._password,
                "password2": proto_user._password,
            }
        )

        assert form.is_valid()
        assert form.clean_username() == proto_user.username

        # Creating a user.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user._password,
                "password2": proto_user._password,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors


class TestSalaryModelForm(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_blank_data(self):
        form = SalaryModelForm({})

        self.assertFalse(form.is_valid())
        self.assertDictEqual(form.errors, {
            'amount': ['This field is required.'],
            'kind': ['This field is required.'],
            'user': ['This field is required.'],
        })

    def test_valid_data(self):
        form = SalaryModelForm({
            'amount': 1000,
            'kind': 1,
            'user': self.user.pk
        })
        self.assertTrue(form.is_valid())

        salary = form.save()
        self.assertEqual(salary.amount, 1000)
        self.assertEqual(salary.get_kind_display(), "NET")
        self.assertEqual(salary.user.id, self.user.pk)
        self.assertEqual(salary.change_at, None)


class TestCorpsModelForm(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_blank_data(self):
        form = CorpsModelForm({})

        self.assertFalse(form.is_valid())
        self.assertDictEqual(form.errors, {
            'name': ['This field is required.'],
            'description': ['This field is required.'],
        })

    def test_valid_data(self):
        form = CorpsModelForm({
            'name': "ADMINISTRATION PENITENTIAIRE",
            'description': "_"
        })
        print("form.errors = ", form.errors)
        self.assertTrue(form.is_valid())

        corps = form.save()
        self.assertEqual(corps.name, "ADMINISTRATION PENITENTIAIRE")
        self.assertEqual(corps.description, "_")
