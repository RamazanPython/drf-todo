from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'mid_name',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'mid_name',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
        )
