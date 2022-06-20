from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'deadline',
        'is_done',
        'created_by',
        'created_date',
        'updated_date',
    )
    list_editable = (
        'is_done',
    )
    list_filter = (
        'is_done',
    )
    search_fields = (
        'id',
        'title',
        'description',
    )
    autocomplete_fields = (
        'created_by',
    )
