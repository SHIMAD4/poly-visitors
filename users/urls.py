from django.contrib.auth import views as auth_views
from django.urls import path

from users.views import Register
from . import views

urlpatterns = [
    path("", views.profile),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("register", Register.as_view(), name="register"),
]
