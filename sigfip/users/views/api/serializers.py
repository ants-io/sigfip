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
