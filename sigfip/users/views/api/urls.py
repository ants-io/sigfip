from django.urls import path, include

from rest_framework import routers

from . import viewsets


router = routers.DefaultRouter()

router.register(r'documents_categories', viewsets.DocumentCategoryViewSet)
router.register(r'loan_categories', viewsets.LoanRequestDocumentViewSet)
router.register(r'prepayments_table', viewsets.PrepaymentTableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
