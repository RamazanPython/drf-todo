from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'mid_name',
        'is_superuser',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'is_staff',
        'is_active',
    )
    list_editable = (
        'is_superuser',
        'is_staff',
        'is_active',
    )
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
                'first_name',
                'last_name',
                'mid_name',
                'is_superuser',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_staff',
                'is_active'
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'mid_name',
                'is_superuser',
                'is_staff',
                'is_active'
            )
        }),
    )
    search_fields = (
        'email',
    )
    ordering = (
        'email',
    )


admin.site.register(User, CustomUserAdmin)
