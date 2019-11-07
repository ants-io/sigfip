import pytest
from django.conf import settings
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_detail(user: settings.AUTH_USER_MODEL):
    assert (
        reverse("app:users:detail", kwargs={"username": user.username})
        == f"/users/{user.username}/"
    )
    assert resolve(f"/users/{user.username}/").view_name == "app:users:detail"


def test_update():
    assert reverse("app:users:profile") == "/users/~update/"
    assert resolve("/users/~update/").view_name == "app:users:profile"


def test_redirect():
    assert reverse("app:users:redirect") == "/users/~redirect/"
    assert resolve("/users/~redirect/").view_name == "app:users:redirect"
