# admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from import_export.admin import ExportActionMixin

from .models import Dormitory, Statement, VisitHistory


class StatementStudentInline(admin.TabularInline):
    model = Statement.student.through  # pylint: disable=no-member
    extra = 1


class StatementAdmin(ExportActionMixin, admin.ModelAdmin):
    inlines = [StatementStudentInline]
    list_display = ("title", "payment", "status", "date")
    filter_horizontal = ["student"]
    list_filter = ("status", "date")
    date_hierarchy = "date"
    search_fields = ["title", "status"]

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": ("title", "payment", "status", "date", "file"),
            },
        ),
        (
            "Связанные студенты",
            {
                "fields": ("student",),
            },
        ),
    )


class DormitoryStudentInline(admin.TabularInline):
    model = Dormitory.student.through  # pylint: disable=no-member
    extra = 1


class DormitoryCommandantInline(admin.TabularInline):
    model = Dormitory.commandant.through  # pylint: disable=no-member
    extra = 1


class DormitoryAdmin(ExportActionMixin, admin.ModelAdmin):
    inlines = [DormitoryStudentInline, DormitoryCommandantInline]
    list_display = ("title", "street")
    filter_horizontal = ["student", "commandant"]
    list_filter = ("title", "street")
    search_fields = ["title", "street"]

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": ("title", "street"),
            },
        ),
        (
            "Связанные студенты и коменданты",
            {
                "fields": ("student", "commandant"),
            },
        ),
    )


class VisitHistoryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("statement_link", "day_of_visit")
    search_fields = ["statement__title"]
    list_filter = ("day_of_visit",)

    fieldsets = (
        (
            "Связанное заявление",
            {
                "fields": ("statement",),
            },
        ),
        (
            "Дата посещения",
            {
                "fields": ("day_of_visit",),
            },
        ),
    )

    def statement_link(self, obj):
        statement_url = reverse("admin:main_statement_change", args=[obj.statement.id])
        return format_html('<a href="{}">{}</a>', statement_url, obj.statement.title)

    statement_link.allow_tags = True
    statement_link.short_description = "Statement"


admin.site.register(Statement, StatementAdmin)
admin.site.register(Dormitory, DormitoryAdmin)
admin.site.register(VisitHistory, VisitHistoryAdmin)
