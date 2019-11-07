from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView, ListView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .. import forms, models
from . import mixins

User = get_user_model()


class UserMixin(mixins.PageMixin):
    page = {
        'title': 'User',
        'namespaces': {
            'create': 'app:users:create',
            'update': 'app:users:update',
            'delete': 'app:users:delete',
            'detail': 'app:users:detail',
            'list': 'app:users:list',
        },
        'field_list': [
            {'name': 'first_name', 'label': 'Prénom'},
            {'name': 'last_name', 'label': 'Nom'},
            {'name': 'registration_number', 'label': 'Matricule'},
            {'name': 'registration_date', 'label': 'Date d\'entrée'},
            {'name': 'retirement_age', 'label': 'Retraite'},
            {'name': 'ministry', 'label': 'Ministère'},
            {'name': 'paying_org', 'label': 'Organisme Payeur'},
            {'name': 'birth_date', 'label': 'Date naissance'},
            {'name': 'phone', 'label': 'Téléphone'}
        ]
    }


class UserListView(LoginRequiredMixin, UserMixin, ListView):

    model = User


user_list_view = UserListView.as_view()


class UserDetailView(LoginRequiredMixin, UserMixin, mixins.UserDetailMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserCreateView(LoginRequiredMixin, CreateView):

    model = User
    form_class = forms.UserForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.registration_number
        user.save()
        return super().form_valid(form)


user_create_view = UserCreateView.as_view()


class UserProfileView(LoginRequiredMixin, UpdateView):

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
        'paying_org',
        'salary',
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


user_profile_view = UserProfileView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = forms.UserForm

    def get_success_url(self):
        return reverse("app:users:detail", kwargs={"username": self.request.user.username})

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("app:users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()


class UserDeleteView(LoginRequiredMixin, UserMixin, DeleteView):

    model = User
    success_url = reverse_lazy('app:users:list')


users_delete_view = UserDeleteView.as_view()
