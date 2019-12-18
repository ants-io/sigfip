from rest_framework import serializers

from ... import models


class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = models.DocumentCategory
        fields = ['id', 'name', 'description', 'required_number']


class LoadRequestCategorySerializer(serializers.ModelSerializer):
    documents = DocumentCategorySerializer(many=True, read_only=True)

    class Meta:

        model = models.RequestCategory
        fields = ['id', 'name', 'documents']


class PrepaymentTableSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.PrepaymentTable
        fields = [
            'id', 'loan_amount', 'duration', 'monthly_withdrawal',
            'recoverable_third_party', 'minimal_salary'
        ]


class CorpsSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Corps
        fields = '__all__'


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Ministry
        fields = '__all__'


class PayingOrgSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.PayingOrg
        fields = '__all__'


class RequestCategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = models.RequestCategory
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    corps = CorpsSerializer(many=False, read_only=True)

    class Meta:

        model = models.Grade
        fields = '__all__'


class SmallLoanSerializer(serializers.ModelSerializer):
    category = RequestCategorySerializer(many=False, read_only=True)

    class Meta:
        model = models.Request
        fields = [
            'id',
            'submit_date',
            'status',
            'amount_awarded',
            'amount_requested',
            'monthly_payment_number',
            'category',
        ]


class UserSerializer(serializers.ModelSerializer):
    grade = GradeSerializer(many=False, read_only=True)
    latest_loan = SmallLoanSerializer(many=False, read_only=True)
    ministry = MinistrySerializer(many=False, read_only=True)
    paying_org = PayingOrgSerializer(many=False, read_only=True)
    loans = SmallLoanSerializer(many=True, read_only=True)

    class Meta:

        model = models.User
        fields = [
            'id', 'first_name', 'last_name', 'birth_date', 'birth_place',
            'sex', 'registration_number', 'registration_date', 'cni', 'salary',
            'address', 'postal_box', 'phone', 'grade', 'ministry',
            'paying_org', 'age', 'retirement_age',
            'last_loan_remaining_months', 'last_loan_required_months',
            'latest_loan', 'loans'
        ]


class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    treatment_agent = UserSerializer(many=False, read_only=True)
    category = RequestCategorySerializer(many=False, read_only=True)

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
