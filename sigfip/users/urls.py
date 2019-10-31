from django.urls import path, include

from sigfip.users.views.users import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

from .views import corps as corps_views

app_name = "app"
users_urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]

corps_urlpatterns = [
    path("list/", view=corps_views.corps_list_view, name="list"),
    path("create/", view=corps_views.corps_create_view, name="create"),
    path("<int:pk>/update/", view=corps_views.corps_update_view, name="update"),
    path("<int:pk>/delete/", view=corps_views.corps_delete_view, name="delete"),
]

urlpatterns = [
    path(r'users/', include((users_urlpatterns, app_name), namespace='users'),),
    path(r'corps/', include((corps_urlpatterns, app_name), namespace='corps'),),
]
