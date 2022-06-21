from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django_rest_passwordreset.models import ResetPasswordToken

from typing import Any

from users.celery_tasks import send_password_reset_email_task


@receiver(reset_password_token_created)
def password_reset_token_created(
        sender: Any,
        instance: Any,
        reset_password_token: ResetPasswordToken,
        *args,
        **kwargs
) -> None:
    user = reset_password_token.user
    send_password_reset_email_task.apply_async(
        kwargs={
            'user_id': user.pk,
        }
    )
