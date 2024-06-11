from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from swagger import urlpatterns as swagger_urls

from main.views import StatementViewSet, DormitoryViewSet

router = routers.SimpleRouter()
router.register(r'statement', StatementViewSet)
router.register(r'dormitory', DormitoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("users/", include("users.urls"), name="users"),
    path("api/v1/", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + swagger_urls
