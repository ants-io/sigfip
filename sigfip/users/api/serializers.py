from rest_framework import serializers

from ..models import *


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'


class CorpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corps
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = '__all__'


class PayingOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayingOrg
        fields = '__all__'


class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = '__all__'


class RequestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestCategory
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class SlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slip
        fields = ['id', 'name', 'description', 'classed_date', 'responsible']
