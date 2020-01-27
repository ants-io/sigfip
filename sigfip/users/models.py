from django.db import models
from django.db.models import Sum
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
from model_utils.fields import StatusField
from model_utils import Choices

from .behaviours import (NameField, TimeStampedField, calculate_age)


class User(AbstractUser):
    first_name = CharField(_("Prénom"), blank=True, null=True, max_length=255)
    last_name = CharField(_("Nom"), blank=True, null=True, max_length=255)
    birth_date = DateField(_("Date de naissance"), blank=True, null=True)
    birth_place = CharField(_("Lieu de naissance"),
                            blank=True,
                            null=True,
                            max_length=255)
    sex = IntegerField(_("Sexe"),
                       choices=(
                           (0, _("Féminin")),
                           (1, _("Masculin")),
                       ),
                       default=1)
    registration_number = CharField(_("Matricule"),
                                    blank=True,
                                    null=True,
                                    max_length=100)
    registration_date = DateField(_("Date d'entrée"), blank=True, null=True)
    cni = CharField(_("Numéro Carte d'identité"),
                    blank=True,
                    null=True,
                    max_length=100)
    retirement_age = IntegerField(_("Age de la retraite"), default=60)
    salary = FloatField(_("Salaire"), default=0)
    address = TextField(
        _("Adresse"),
        blank=True,
        null=True,
    )
    postal_box = CharField(_("Boite postale"),
                           blank=True,
                           null=True,
                           max_length=20)
    phone = CharField(_("Mobile / Téléphone"),
                      blank=True,
                      null=True,
                      max_length=20)
    profession = ForeignKey('Profession',
                            verbose_name=_("Profession"),
                            blank=True,
                            null=True,
                            on_delete=models.CASCADE)
    grade = ForeignKey('Grade',
                       blank=True,
                       null=True,
                       verbose_name=_("Grade"),
                       on_delete=models.CASCADE)
    ministry = ForeignKey('Ministry',
                          blank=True,
                          null=True,
                          verbose_name=_("Ministère"),
                          on_delete=models.CASCADE)
    paying_org = ForeignKey('PayingOrg',
                            blank=True,
                            null=True,
                            verbose_name=_("Organisme payeur"),
                            on_delete=models.CASCADE)

    def age(self):
        age = calculate_age(self.birth_date)
        return f'{age} ans' if age else '_'

    def retirement_age(self):
        return self.grade.retired_to if self.grade else 60

    def latest_loan(self):
        return self.request_set.first()

    def last_loan_remaining_months(self):
        return 0

    def last_loan_required_months(self):
        return 0

    def full_name(self):
        return f'{self.name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("app:users:detail", kwargs={"username": self.username})

    def loans(self):
        return self.request_set.order_by('-created_at')

    @property
    def past_loans_amount(self):
        amount = self.request_set\
            .filter(status='accepted')\
            .aggregate(total=Sum('amount_awarded'))\
            .get('total')

        return amount if amount else 0

    @property
    def available_loans(self):
        return 5000000 - self.past_loans_amount


class Salary(TimeStampedField):
    """
    Model that track all user's salary evolution.
    """

    # user = ForeignKey(User, on_delete=models.CASCADE)
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
    corps = ForeignKey(Corps,
                       verbose_name=_("Corps"),
                       on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'grades'


class Profession(NameField):
    """
    Model that store all existing Corps in System.
    """
    pass


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


class Slip(NameField, TimeStampedField):

    classed_date = DateField(_("Date de classification"))
    responsible = ForeignKey(User, on_delete=models.CASCADE)


class Request(TimeStampedField):
    """
    Application for user to have a loan.
    """
    STATUS_CHOICES = Choices('pending', 'accepted', 'archived', 'cancelled',
                             'frozen', 'rejected')

    amount_requested = FloatField(_("Montant demandé"))
    amount_awarded = FloatField(_("Montant prêt accordé"),
                                blank=True,
                                null=True)
    amount_to_repay = FloatField(_("Montant à rembourser"),
                                 blank=True,
                                 null=True)
    monthly_payment_number = FloatField(_("C. Nombre de mensualité"),
                                        blank=True,
                                        null=True)
    quota = FloatField(_("D. Quotité = A / 3"), blank=True, null=True)
    withholding = FloatField(
        _("E. Précompte = Montant prêt / <span id='id_n_months'>C</span>"),
        blank=True,
        null=True)
    submit_date = DateField(_("Date de dépôt de la demande"),
                            blank=True,
                            null=True)
    proceed_date = DateField(_("Date de traitement"), blank=True, null=True)
    post_reference = CharField(_("Référence courier"),
                               max_length=20,
                               blank=True,
                               null=True)
    convention = CharField(_("Convention"),
                           max_length=100,
                           blank=True,
                           null=True)
    category = ForeignKey(RequestCategory,
                          verbose_name=_("Catégorie de la demande"),
                          on_delete=models.CASCADE)
    observations = TextField(_("Observations"), blank=True)
    status = StatusField(choices_name='STATUS_CHOICES')
    user = ForeignKey(User, verbose_name=_("Agent"), on_delete=models.CASCADE)
    slip = ForeignKey(Slip,
                      verbose_name=_("Bordereau"),
                      on_delete=models.CASCADE)
    treatment_agent = ForeignKey(User,
                                 verbose_name=_("Agent de traitement"),
                                 related_name='treatment_agent',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

    @property
    def documents(self):
        return self.document_set.all()

    @property
    def loan_file(self):
        documents = self.document_set.all()
        for doc in documents:
            if doc.provided_number < doc.document_category.required_number:
                return False
        return True

    def get_absolute_url(self):
        return reverse("app:loans:detail", kwargs={"pk": self.pk})


class Document(TimeStampedField):
    """
    Document given by user to apply for a loan.
    """
    physical_document = FileField(_("Document"), blank=True, null=True)
    provided_number = IntegerField(_("Nombre fourni"), default=0)
    reference = CharField(_("Nombre exigé"),
                          max_length=255,
                          blank=True,
                          null=True)
    document_date = DateField(_("Date pièce"), blank=True, null=True)
    document_category = ForeignKey(DocumentCategory,
                                   verbose_name=_("Document de reference"),
                                   on_delete=models.CASCADE)
    request = ForeignKey(Request,
                         verbose_name=_("Demande correspondante"),
                         on_delete=models.CASCADE)


class PrepaymentTable(TimeStampedField):
    loan_amount = FloatField(_("Montant du prêt"))
    duration = FloatField(_("Durée en années"))
    monthly_withdrawal = IntegerField(_("Prélévement mensuel"))
    recoverable_third_party = FloatField(_("Tiers saisissable"))
    minimal_salary = FloatField(_("Salaire minimum"))

    class Meta:

        verbose_name_plural = 'prepayment_table'

    def __str__(self):
        return f'Loan: {self.loan_amount}, duration: {self.duration}, minimal salary: {self.minimal_salary}'
