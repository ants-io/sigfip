from django.contrib.auth import get_user_model, forms as from_auth_forms
from django import forms
from django.forms import ModelForm, Textarea, TextInput
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from . import models, forms_mixins as mixins

User = get_user_model()


class UserChangeForm(from_auth_forms.UserChangeForm):
    class Meta(from_auth_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(from_auth_forms.UserCreationForm):

    error_message = from_auth_forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(from_auth_forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class UserForm(forms.ModelForm):

    class Meta:
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
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'birth_date': forms.TextInput(attrs={
                'class': 'filter__group__field date'
            }),
            'birth_place': forms.TextInput(attrs={
                'class': 'filter__group__field date'
            }),
            'sex': forms.Select(attrs={
                'class': 'filter__group__field'
            }),
            'registration_number': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'registration_date': forms.TextInput(attrs={
                'class': 'filter__group__field date'
            }),
            'cni': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'address': forms.Textarea(attrs={
                'class': 'filter__group__textarea',
                'rows': 3
            }),
            'postal_box': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'grade': forms.Select(attrs={
                'class': 'filter__group__field'
            }),
            'ministry': forms.Select(attrs={
                'class': 'filter__group__field'
            }),
            'paying_org': forms.Select(attrs={
                'class': 'filter__group__field'
            }),
            'salary': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
        }


class SalaryModelForm(forms.ModelForm):

    class Meta:
        model = models.Salary
        fields = ['kind', 'amount', 'change_at']
        widgets: {
            'kind': forms.TextInput(),
            'amount': forms.TextInput(),
            'change_at': forms.TextInput(),
        }


class CorpsModelForm(mixins.NameFormFields):

    class Meta(mixins.NameFormFields.Meta):

        model = models.Corps
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'description': forms.Textarea(attrs={
                'class': 'filter__group__textarea'
            })
        }


class GradeModelForm(mixins.NameFormFields):

    class Meta(mixins.NameFormFields.Meta):

        model = models.Grade
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'retired_to': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'description': forms.Textarea(attrs={
                'class': 'filter__group__textarea',
                'rows': 3
            }),
            'corps': forms.Select(attrs={
                'class': 'filter__group__field'
            })
        }


class MinistryModelForm(mixins.NameFormFields):

    class Meta(mixins.NameFormFields.Meta):

        model = models.Ministry
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'description': forms.Textarea(attrs={
                'class': 'filter__group__textarea'
            })
        }


class PayingOrgModelForm(mixins.NameFormFields):

    class Meta(mixins.NameFormFields.Meta):

        model = models.PayingOrg
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'description': forms.Textarea(attrs={
                'class': 'filter__group__textarea'
            })
        }


class DocumentCategoryModelForm(mixins.NameFormFields):

    class Meta(mixins.NameFormFields.Meta):

        fields = '__all__'
        model = models.DocumentCategory
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'required_number': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'description': forms.Textarea(attrs={
                'class': 'filter__group__textarea'
            })
        }


class RequestCategoryModelForm(mixins.NameFormFields):

    class Meta(mixins.NameFormFields.Meta):

        fields = '__all__'
        model = models.RequestCategory
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'documents': forms.SelectMultiple(attrs={
                'class': 'filter__group__textarea'
            }),
            'description': forms.Textarea(attrs={
                'class': 'filter__group__textarea',
                'rows': '3'
            })
        }


class PrepaymentTableForm(mixins.NameFormFields):

    class Meta:

        fields = '__all__'
        model = models.PrepaymentTable
        widgets = {
            'loan_amount': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'duration': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'monthly_withdrawal': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'recoverable_third_party': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'minimal_salary': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
        }


class LoanForm(ModelForm):

    class Meta:

        fields = [
            'user',
            'amount_requested',
            'category',
            'observations'
        ]
        model = models.Request
        widgets = {
            'amount_requested': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'category': forms.Select(attrs={
                'class': 'filter__group__field'
            }),
            'observations': forms.Textarea(attrs={
                'class': 'filter__group__textarea',
                'rows': 4
            })
        }


class LoanDetailForm(ModelForm):

    class Meta:

        fields = '__all__'
        model = models.Request
        widgets = {
            'amount_requested': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'amount_awarded': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'amount_to_repay': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'monthly_payment_number': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'quota': forms.TextInput(attrs={
                'class': 'filter__group__field',
                'disabled': True
            }),
            'withholding': forms.TextInput(attrs={
                'class': 'filter__group__field',
                'disabled': True
            }),
            'status': forms.Select(attrs={
                'class': 'filter__group__field'
            }),
            'category': forms.Select(attrs={
                'class': 'filter__group__field'
            }),
            'observations': forms.Textarea(attrs={
                'class': 'filter__group__textarea',
                'rows': 4
            }),
            'date': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'treatment_date': forms.TextInput(attrs={
                'class': 'filter__group__field'
            }),
            'treatment_agent': forms.Select(attrs={
                'class': 'filter__group__field'
            }),
        }


class DocumentForm(ModelForm):

    class Meta:

        fields = '__all__'
        model = models.Document
