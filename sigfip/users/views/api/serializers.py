from rest_framework import serializers

from ... import models


class DocumentCategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = models.DocumentCategory
        fields = ['id', 'name', 'description', 'required_number']


class LoadRequestCategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = models.RequestCategory
        fields = ['id', 'name']


class PrepaymentTableSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.PrepaymentTable
        fields = ['id', 'loan_amount', 'duration', 'monthly_withdrawal', 'recoverable_third_party', 'minimal_salary']


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.User
        fields = [
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'birth_place',
            'sex',
            'registration_number',
            'registration_date',
            'cni',
            'salary',
            'address',
            'postal_box',
            'phone',
            'grade',
            'ministry',
            'paying_org',
            'age',
            'retirement_age',
            'last_loan_remaining_months',
            'last_loan_required_months',
        ]


class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = models.Request
        fields = [
            'id',
            'date',
            'user',
            'status',
            'amount_requested',
            'amount_awarded',
            'amount_to_repay',
            'monthly_payment_number',
            'quota',
            'withholding',
            'treatment_date',
            'post_reference',
            'category',
            'observations',
            'status',
            'treatment_agent',
        ]
