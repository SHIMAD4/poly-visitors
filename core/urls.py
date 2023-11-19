from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from main.views import StatementApiView, DormitoryApiView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("users/", include("users.urls"), name="users"),
    path("api/v1/statementlist/", StatementApiView.as_view()),
    path("api/v1/dormitorylist/", DormitoryApiView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
