import django_filters

from . import models


class UserFilter(django_filters.FilterSet):

    class Meta:

        model = models.User
        fields = {
            'registration_number': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
        }
