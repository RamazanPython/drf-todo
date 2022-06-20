from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.managers import UserManager
from utils.models import AbstractTimeTrackable


class User(AbstractBaseUser,
           PermissionsMixin,
           AbstractTimeTrackable):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_('Имя')
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_('Фамилия')
    )
    mid_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_('Отчество')
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        null=True,
        verbose_name=_('Электронная почта')
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name=_('Суперпользователь')
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Сотрудник')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Активный')
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self) -> str:
        return self.email
