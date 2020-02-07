from rest_framework import serializers

from ... import models, forms


class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = models.DocumentCategory
        fields = ['id', 'name', 'description', 'required_number']


class LoadRequestCategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = models.RequestCategory
        fields = ['id', 'name', 'description', 'documents']


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


class SmallRequestCategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = models.RequestCategory
        fields = ['id', 'name']


class GradeSerializer(serializers.ModelSerializer):
    corps = CorpsSerializer(many=False, read_only=True)

    class Meta:

        model = models.Grade
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Profession
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):

    document_category = DocumentCategorySerializer(many=False, read_only=True)

    class Meta:
        model = models.Document
        fields = [
            'id', 'physical_document', 'provided_number', 'reference',
            'document_date', 'document_category'
        ]


class ExtraSmallLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Request
        fields = [
            'id',
            'created_at',
            'status',
            'amount_awarded',
        ]


class SmallLoanSerializer(serializers.ModelSerializer):
    doc_category = SmallRequestCategorySerializer(many=False, read_only=True)

    class Meta:
        model = models.Request
        fields = [
            'id',
            'submit_date',
            'status',
            'amount_awarded',
            'amount_requested',
            'monthly_payment_number',
            'doc_category',
            'state',
        ]


class UserSerializer(serializers.ModelSerializer):
    # grade = GradeSerializer(many=False, read_only=True)
    # ministry = MinistrySerializer(many=False, read_only=True)
    # paying_org = PayingOrgSerializer(many=False, read_only=True)
    # profession = ProfessionSerializer(many=True, read_only=True)
    latest_loan = SmallLoanSerializer(many=False, read_only=True)
    loans = SmallLoanSerializer(many=True, read_only=True)

    class Meta:

        model = models.User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'birth_date',
            'birth_place', 'sex', 'registration_number', 'registration_date',
            'cni', 'salary', 'address', 'postal_box', 'phone', 'grade',
            'ministry', 'paying_org', 'age', 'retirement_age',
            'last_loan_remaining_months', 'last_loan_required_months',
            'latest_loan', 'loans', 'profession'
        ]


class SmallUserSerializer(serializers.ModelSerializer):
    grade = GradeSerializer(many=False, read_only=True)
    latest_loan = SmallLoanSerializer(many=False, read_only=True)

    class Meta:

        model = models.User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'grade',
            'registration_number', 'latest_loan', 'salary'
        ]


class ExtraSmallUserSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'registration_number',
        ]


class LoanSerializer(serializers.ModelSerializer):
    user = SmallUserSerializer(many=False, read_only=True)
    treatment_agent = SmallUserSerializer(many=False, read_only=True)
    doc_category = RequestCategorySerializer(many=False, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)

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
            'doc_category',
            'observations',
            'status',
            'treatment_agent',
            'documents',
            'convention',
            'slip',
            'state',
        ]

    def create(self, validate_data):
        data = self.context.get('request').data
        form = forms.LoanForm(data)
        document_ids = []
        provided_numbers = []
        references = []
        document_dates = []

        if form.is_valid():
            model = form.save(commit=False)

            if not model.monthly_payment_number:
                model.monthly_payment_number = line.duration * 12

            model.amount_awarded = model.amount_requested
            model.amount_to_repay = model.amount_awarded
            model.quota = model.user.salary / 3
            model.withholding = model.amount_awarded / model.monthly_payment_number
            # model.treatment_agent_id = data['treatment_agent']
            model.save()

            for document in data['documents']:
                doc_form = forms.DocumentForm({
                    'request':
                    model.id,
                    'document_category':
                    document['id'],
                    'provided_number':
                    document['provided_number'],
                    'reference':
                    document['reference'],
                    'document_date':
                    document['document_date']
                })

                # Handle when it's false.
                if doc_form.is_valid():
                    doc_form.save()
            return model

    def update(self, instance, validated_data):
        data = self.context.get('request').data
        form = forms.LoanDetailForm(data, instance=instance)
        print({'form_is_valid ?': form.errors})
        if form.is_valid():
            form.save()

        for document in data['documents']:
            doc = models.Document.objects.get(pk=document['id'])
            doc.provided_number = document['provided_number']
            doc.reference = document['reference']
            doc.document_date = document['document_date']
            doc.save()

        return instance