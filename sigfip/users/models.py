from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField,
    DateField,
    FileField,
    FloatField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    OneToOneField,
    TextField,
)
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from model_utils.models import StatusModel
from model_utils import Choices

from .behaviours import (NameField, TimeStampedField)


class User(AbstractUser):
    first_name = CharField(_("Prénom"), blank=True, null=True, max_length=255)
    last_name = CharField(_("Nom"), blank=True, null=True, max_length=255)
    birth_date = DateField(_("Date de naissance"), blank=True, null=True)
    birth_place = CharField(_("Lieu de naissance"), blank=True, null=True, max_length=255)
    sex = IntegerField(_("Sexe"), choices=(
        (0, _("Féminin")),
        (1, _("Masculin")),
    ), default=1)
    registration_number = CharField(_("Matricule"), blank=True, null=True, max_length=100)
    registration_date = DateField(_("Date d'entrée"), blank=True, null=True)
    cni = CharField(_("Numéro Carte d'identité"), blank=True, null=True, max_length=100)
    retirement_age = IntegerField(_("Age de la retraite"), default=60)

    def full_name(self):
        return f'{self.name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("app:users:detail", kwargs={"username": self.username})


class Salary(TimeStampedField):
    """
    Model that track all user's salary evolution.
    """

    user = ForeignKey(User, on_delete=models.CASCADE)
    kind = IntegerField(_("Type"), choices=(
        (0, _("Brute")),
        (1, _("NET")),
    ))
    amount = FloatField(_("Montant"))
    change_at = DateField(_("Date mise à jour"), blank=True, null=True)

    class Meta:
        verbose_name_plural = 'salaries'

    def __str__(self):
        return f'{self.user.full_name}: {self.amount * 12} FCFA Annual.'


class Corps(NameField):
    """
    Model that store all existing Corps in System.
    """

    class Meta:
        verbose_name_plural = 'corps'


class Grade(NameField):
    """
    Model that store all existing Grades in System.
    """

    retired_to = IntegerField(_("Retraité à"))
    corps = ForeignKey(Corps, verbose_name=_("Corps"), on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'grades'


class Ministry(NameField):
    """
    Model that store all existing Corps in System.
    """

    class Meta:
        verbose_name_plural = 'ministers'


class PayingOrg(NameField, TimeStampedField):
    """
    Model that store all existing paying org in System, 
    where the related user get paid from.
    """

    class Meta:
        verbose_name_plural = 'paying_orgs'


class AdditionalInformation(TimeStampedField):
    """
    Additionnal informations for user.
    """
    user = OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)
    address = TextField(_("Adresse"))
    postal_box = CharField(_("Boite postale"), max_length=20)
    phone = CharField(_("Mobile / Téléphone"), max_length=20)
    grade = ForeignKey(
        Grade, verbose_name=_("Grade"), on_delete=models.CASCADE)
    ministry = ForeignKey(
        Ministry, verbose_name=_("Ministère"), on_delete=models.CASCADE)
    paying_org = ForeignKey(
        PayingOrg,
        verbose_name=_("Organisme payeur"),
        on_delete=models.CASCADE)

    def __str__(self):
        return self.user.full_name

    def get_absolute_url(self):
        return reverse("app:users:detail", kwargs={"username": self.username})


class DocumentCategory(NameField, TimeStampedField):
    """
    All Document categories. (CNI, Passport, 'Birth act', ...)
    """
    required_number = IntegerField(_("Nombre exigé"), default=1)

    class Meta:
        verbose_name_plural = 'document_categories'


class RequestCategory(NameField, TimeStampedField):
    """
    Request categories and all required document for each category.
    """
    documents = ManyToManyField(DocumentCategory)

    class Meta:
        verbose_name_plural = 'request_categories'


class Request(TimeStampedField):
    """
    Application for user to have a loan.
    """
    amount_requested = FloatField(_("Montant demandé"))
    amount_awarded = FloatField(_("Montant accordé"))
    date = DateField(_("Date de dépôt de la demande"))
    post_reference = CharField(_("Référence courier"), max_length=20)
    category = ForeignKey(
        RequestCategory,
        verbose_name=_("Catégorie de la demande"),
        on_delete=models.CASCADE)
    observations = TextField(_("Observations"), blank=True)
    status = Choices('accepted', 'archived', 'frozen', 'rejected',)

    class Meta:
        ordering = ['created_at']


class Document(TimeStampedField):
    """
    Document given by user to apply for a loan.
    """
    physical_document = FileField(_("Document"), blank=True, null=True)
    required_number = IntegerField(_("Nombre exigé"), default=0)
    reference = CharField(_("Nombre exigé"), max_length=255, blank=True, null=True)
    document_category = ForeignKey(
        DocumentCategory,
        verbose_name=_("Document de reference"),
        on_delete=models.CASCADE)
    request = ForeignKey(
        Request,
        verbose_name=_("Demande correspondante"),
        on_delete=models.CASCADE)
