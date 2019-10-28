import pytest
from django.conf import settings
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_detail(user: settings.AUTH_USER_MODEL):
    assert (
        reverse("users:list:detail", kwargs={"username": user.username})
        == f"/users/{user.username}/"
    )
    assert resolve(f"/users/{user.username}/").view_name == "users:list:detail"


def test_update():
    assert reverse("users:list:update") == "/users/~update/"
    assert resolve("/users/~update/").view_name == "users:list:update"


def test_redirect():
    assert reverse("users:list:redirect") == "/users/~redirect/"
    assert resolve("/users/~redirect/").view_name == "users:list:redirect"
