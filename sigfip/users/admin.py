from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from . import models

from sigfip.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {
        "fields": ('birth_date', )
    }), ) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "first_name", "last_name", "is_superuser"]
    search_fields = ["first_name", "last_name", "email"]


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = [
        "amount_requested",
        "amount_awarded",
        "monthly_payment_number",
        "submit_date",
        "proceed_date",
        "category",
        "status",
        "user",
        "treatment_agent",
    ]
