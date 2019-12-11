from django.urls import path, include

from rest_framework import routers

from . import viewsets, api_views


router = routers.DefaultRouter()

router.register(r'documents_categories', viewsets.DocumentCategoryViewSet)
router.register(r'loan_categories', viewsets.LoanRequestDocumentViewSet)
router.register(r'prepayments_table', viewsets.PrepaymentTableViewSet)

urlpatterns = [
    path('searching/', api_views.searching, name='searching'),
    path('', include(router.urls)),
]
