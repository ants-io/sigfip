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


class SalaryModelForm(forms.ModelForm):

    class Meta:
        model = models.Salary
        fields = ['user', 'kind', 'amount', 'change_at']
        widgets: {
            'kind': forms.TextInput(),
            'amount': forms.TextInput(),
            'change_at': forms.TextInput(),
        }


class CorpsModelForm(mixins.NameFormFields):

    class Meta:

        model = models.Corps
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(),
            'description': Textarea(),
        }
