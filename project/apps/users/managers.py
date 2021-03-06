from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(
            self,
            email: str,
            password: str,
            **extra_fields
    ) -> settings.AUTH_USER_MODEL:
        if not email:
            raise ValueError(_("not_email"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
            self,
            email: str,
            password: str,
            **extra_fields
    ) -> settings.AUTH_USER_MODEL:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("is_staff"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("is_superuser"))

        return self.create_user(email, password, **extra_fields)
