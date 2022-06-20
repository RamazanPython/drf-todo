from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractTimeTrackable, AbstractCreatedBy


class Task(AbstractTimeTrackable, AbstractCreatedBy):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Заголовок')
    )
    description = models.TextField(
        verbose_name=_('Описание')
    )
    deadline = models.DateTimeField(
        verbose_name=_('Срок исполнения')
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name=_('Выполнено')
    )

    class Meta:
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')

    def __str__(self) -> str:
        return f'Задача с ID {self.id}'
