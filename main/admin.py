from django.contrib import admin
from import_export.admin import ExportActionMixin

from .models import Dormitory, Statement, VisitHistory
# Register your models here.


class AdminStatement(ExportActionMixin, admin.ModelAdmin):
    def display_students(self, obj):
        return ", ".join([f"{student.last_name} {student.first_name}" for student in obj.student.all()])

    list_display = ("title", "payment", "status", "date", "display_students")
    filter_horizontal = ["student"]
    list_filter = ("status", "date")
    date_hierarchy = "date"
    search_fields = ["title", "status"]


class AdminVisitHistory(ExportActionMixin, admin.ModelAdmin):
    list_display = ("statement", "day_of_visit")
    search_fields = ["statement"]
    list_filter = ("day_of_visit",)


class AdminDormitory(ExportActionMixin, admin.ModelAdmin):
    def display_students(self, obj):
        return ", ".join([f"{student.last_name} {student.first_name}" for student in obj.student.all()])

    def display_commandants(self, obj):
        return ", ".join([f"{commandant.last_name} {commandant.first_name}" for commandant in obj.commandant.all()])

    list_display = ("title", "street", "display_students", "display_commandants")
    filter_horizontal = ["student", "commandant"]
    list_filter = ("title", "street")
    search_fields = ["title", "street"]


admin.site.register(Statement, AdminStatement)
admin.site.register(Dormitory, AdminDormitory)
admin.site.register(VisitHistory, AdminVisitHistory)
