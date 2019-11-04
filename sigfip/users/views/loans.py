from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .. import forms, models
from . import mixins


class LoanDetailView(
    LoginRequiredMixin,
    # mixins.LoanDetailMixin,
        DetailView):

    model = models.Request


loan_detail_view = LoanDetailView.as_view()
