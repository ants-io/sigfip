# import pytest
# from django.conf import settings
# from django.urls import reverse, resolve

# pytestmark = pytest.mark.django_db


# def test_list(user: settings.AUTH_USER_MODEL):
#     assert (reverse("corps:list") == "/corps/list")
#     assert resolve("/corps/list").view_name = "corps:list"


# def test_create(user: settings.AUTH_USER_MODEL):
#     assert (reverse("corps:create") == "/corps/create")
#     assert resolve("/corps/create").view_name = "corps:create"


# def test_detail(user: settings.AUTH_USER_MODEL):
#     assert (reverse("corps:detail") == "/corps/list")
#     assert resolve("/corps/list").view_name = "corps:list"


# def test_redirect(user: settings.AUTH_USER_MODEL):
#     assert (reverse("corps:list") == "/corps/list")
#     assert resolve("/corps/list").view_name = "corps:list"


# def test_update(user: settings.AUTH_USER_MODEL):
#     assert (reverse("corps:list") == "/corps/list")
#     assert resolve("/corps/list").view_name = "corps:list"


# def test_delete(user: settings.AUTH_USER_MODEL):
#     assert (reverse("corps:list") == "/corps/list")
#     assert resolve("/corps/list").view_name = "corps:list"
