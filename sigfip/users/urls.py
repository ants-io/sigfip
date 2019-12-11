from django.urls import path, include

from sigfip.users.views.users import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    user_list_view,
    user_create_view,
    user_profile_view,
    users_delete_view,
)

from .views import corps as corps_views
from .views import grades as grades_views
from .views import ministers as ministers_views
from .views import paying_orgs as paying_orgs_views
from .views import request_category as request_category_views
from .views import document_category as document_category_views
from .views import loans as loans_views
from .views import prepayments_table as prepayments_table_views

from .views.api.urls import urlpatterns

app_name = "app"
users_urlpatterns = [
    path("list/", view=user_list_view, name="list"),
    path("create/", view=user_create_view, name="create"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~profile/", view=user_profile_view, name="profile"),
    path("<int:pk>/delete/", view=users_delete_view, name="delete"),
    path("<int:pk>/update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]

corps_urlpatterns = [
    path("list/", view=corps_views.corps_list_view, name="list"),
    path("create/", view=corps_views.corps_create_view, name="create"),
    path("<int:pk>/update/", view=corps_views.corps_update_view, name="update"),
    path("<int:pk>/delete/", view=corps_views.corps_delete_view, name="delete"),
]

grades_urlpatterns = [
    path("list/", view=grades_views.grades_list_view, name="list"),
    path("create/", view=grades_views.grades_create_view, name="create"),
    path("<int:pk>/update/", view=grades_views.grades_update_view, name="update"),
    path("<int:pk>/delete/", view=grades_views.grades_delete_view, name="delete"),
]

ministers_urlpatterns = [
    path("list/", view=ministers_views.ministers_list_view, name="list"),
    path("create/", view=ministers_views.ministers_create_view, name="create"),
    path("<int:pk>/update/", view=ministers_views.ministers_update_view, name="update"),
    path("<int:pk>/delete/", view=ministers_views.ministers_delete_view, name="delete"),
]

paying_orgs_urlpatterns = [
    path("list/", view=paying_orgs_views.paying_orgs_list_view, name="list"),
    path("create/", view=paying_orgs_views.paying_orgs_create_view, name="create"),
    path("<int:pk>/update/", view=paying_orgs_views.paying_orgs_update_view, name="update"),
    path("<int:pk>/delete/", view=paying_orgs_views.paying_orgs_delete_view, name="delete"),
]

request_categories_urlpatterns = [
    path("list/", view=request_category_views.request_categories_list_view, name="list"),
    path("create/", view=request_category_views.request_categories_create_view, name="create"),
    path("<int:pk>/update/", view=request_category_views.request_categories_update_view, name="update"),
    path("<int:pk>/delete/", view=request_category_views.request_categories_delete_view, name="delete"),
]

document_categories_urlpatterns = [
    path("list/", view=document_category_views.document_categories_list_view, name="list"),
    path("create/", view=document_category_views.document_categories_create_view, name="create"),
    path("<int:pk>/update/", view=document_category_views.document_categories_update_view, name="update"),
    path("<int:pk>/delete/", view=document_category_views.document_categories_delete_view, name="delete"),
]

loans_urlpatterns = [
    # path("list/", view=document_category_views.document_categories_list_view, name="list"),
    # path("create/", view=document_category_views.document_categories_create_view, name="create"),
    path("<int:pk>/detail/", view=loans_views.loan_detail_view, name="detail"),
    # path("<int:pk>/update/", view=document_category_views.document_categories_update_view, name="update"),
    # path("<int:pk>/delete/", view=document_category_views.document_categories_delete_view, name="delete"),
]

prepayments_table_urlpatterns = [
    path("list/", view=prepayments_table_views.prepayments_table_list_view, name="list"),
    path("create/", view=prepayments_table_views.prepayments_table_create_view, name="create"),
    path("<int:pk>/update/", view=prepayments_table_views.prepayments_table_update_view, name="update"),
    path("<int:pk>/delete/", view=prepayments_table_views.prepayments_table_delete_view, name="delete"),
]

urlpatterns = [
    path('users/', include((users_urlpatterns, app_name), namespace='users')),
    path('loans/', include((loans_urlpatterns, app_name), namespace='loans')),
    path('corps/', include((corps_urlpatterns, app_name), namespace='corps')),
    path('grades/', include((grades_urlpatterns, app_name), namespace='grades')),
    path('api/v1/', include((urlpatterns, app_name), namespace='api')),
    path('ministers/', include((ministers_urlpatterns, app_name), namespace='ministers')),
    path('paying-orgs/', include((paying_orgs_urlpatterns, app_name), namespace='paying_orgs')),
    path('prepayments-table/', include((prepayments_table_urlpatterns, app_name), namespace='prepayments_table')),
    path('request-categories/', include((request_categories_urlpatterns, app_name), namespace='request_categories')),
    path('document-categories/', include((document_categories_urlpatterns, app_name), namespace='document_categories')),
]
