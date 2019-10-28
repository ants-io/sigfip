from django.db import models
from django.db.models import (CharField, DateTimeField, TextField, )
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class NameField(models.Model):
    """
    This abstract model will be inherited by all model which have name and description fields.
    """

    name = CharField(_("Nom"), max_length=255)
    description = TextField(_("Description"))

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return f'{self.name}: {self.description}'


class TimeStampedField(models.Model):
    """
    This abstract model allow to add timestamped fields to every models who need them.
    """

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_at']
