from django.shortcuts import get_object_or_404

# import django_filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from ... import models


class DocumentCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.DocumentCategorySerializer
    queryset = models.DocumentCategory.objects.all()


class LoanRequestDocumentViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.LoadRequestCategorySerializer
    queryset = models.RequestCategory.objects.all()

    # TODO with django filter. If possible
    @action(detail=True)
    def documents(self, request, *args, **kwargs):
        self.object = self.get_object()

        documents = self.object.documents.all()
        serialized_documents = serializers.DocumentCategorySerializer(documents, many=True)

        return Response(serialized_documents.data)
