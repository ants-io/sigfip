from sigfip.users.api.viewsets import *

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from django_filters.views import FilterView

from sigfip.users.filters import UserFilter

from rest_framework import routers

urlpatterns = [
    path("",
         login_required(TemplateView.as_view(template_name="pages/home.html")),
         name="home"),
    path("search/",
         login_required(
             FilterView.as_view(filterset_class=UserFilter,
                                template_name="pages/home.html")),
         name="search"),
    path(settings.ADMIN_URL, admin.site.urls),
    # User ~> App management
    path("", include("sigfip.users.urls", namespace="app")),
    path("accounts/", include("allauth.urls")),
    # path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))
                       ] + urlpatterns
