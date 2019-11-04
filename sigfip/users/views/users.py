from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .. import forms, models
from . import mixins

User = get_user_model()


class UserListView(LoginRequiredMixin, ListView):

    model = User
    template = 'users/users/list.html'


class UserDetailView(LoginRequiredMixin, mixins.UserDetailMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = [
        'first_name',
        'last_name',
        'birth_date',
        'birth_place',
        'sex',
        'registration_number',
        'registration_date',
        'cni',
        'address',
        'postal_box',
        'phone',
        'grade',
        'ministry',
        'paying_org'
    ]

    def get_success_url(self):
        return reverse("app:users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("app:users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
