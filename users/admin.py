from django.contrib import admin
from django.contrib.auth import get_user_model
from import_export.admin import ExportActionMixin

from .models import Commandants, Students

# Register your models here.
User = get_user_model()


class AdminUser(ExportActionMixin, admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
    list_filter = ("email", "last_name")
    search_fields = ["email", "last_name"]


class AdminStudents(ExportActionMixin, admin.ModelAdmin):
    list_display = ("first_name", "last_name", "room")
    list_filter = ("room", "last_name")
    search_fields = ["room", "last_name"]


class AdminCommandants(ExportActionMixin, admin.ModelAdmin):
    list_display = ("first_name", "last_name")


admin.site.register(User, AdminUser)
admin.site.register(Students, AdminStudents)
admin.site.register(Commandants, AdminCommandants)
