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


class CorpsSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Corps
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    corps = CorpsSerializer(many=False, read_only=True)

    class Meta:

        model = models.Grade
        fields = '__all__'


class SmallLoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Request
        fields = [
            'id',
            'submit_date',
            'status',
            'amount_awarded',
            'monthly_payment_number',
        ]


class UserSerializer(serializers.ModelSerializer):
    grade = GradeSerializer(many=False, read_only=True)
    latest_loan = SmallLoanSerializer(many=False, read_only=True)

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
            'latest_loan',
        ]


class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = models.Request
        fields = [
            'id',
            'submit_date',
            'user',
            'status',
            'amount_requested',
            'amount_awarded',
            'amount_to_repay',
            'monthly_payment_number',
            'quota',
            'withholding',
            'proceed_date',
            'post_reference',
            'category',
            'observations',
            'status',
            'treatment_agent',
        ]
