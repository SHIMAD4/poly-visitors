from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("statements", views.statement_home),
    path("settings", views.settings_home),
    path("settings/mail", views.settings_mail, name="settings_mail"),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("users/", include("users.urls"), name="users"),
]
