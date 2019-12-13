from django.urls import path, include

from rest_framework import routers

from . import viewsets, api_views
from ...api import viewsets as vws

router = routers.DefaultRouter()

router.register('corps', vws.CorpsViewSet)
router.register('documents_categories', viewsets.DocumentCategoryViewSet)
router.register('grades', vws.GradeViewSet)
router.register('loans', vws.RequestViewSet)
router.register('loan_categories', viewsets.LoanRequestDocumentViewSet)
router.register('ministries', vws.MinistryViewSet)
router.register('paying_orgs', vws.PayingOrgViewSet)
router.register('prepayments_table', viewsets.PrepaymentTableViewSet)
router.register('users', vws.UserViewSet)
router.register('professions', vws.ProfessionViewSet)

urlpatterns = [
    path('searching/', api_views.searching, name='searching'),
    path('', include(router.urls)),
]
