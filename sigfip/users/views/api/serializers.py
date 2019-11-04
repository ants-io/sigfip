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
