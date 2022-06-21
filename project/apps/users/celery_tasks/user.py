from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django_rest_passwordreset.models import ResetPasswordToken

from celery import shared_task

from users.models import User


@shared_task()
def send_password_reset_email_task(user_id: int) -> None:
    try:
        user = User.objects.get(pk=user_id)
        reset_password_token = ResetPasswordToken.objects.filter(user=user).first()
    except (User.DoesNotExist, ResetPasswordToken.DoesNotExist):
        return

    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'),
        reset_password_token.key
    )

    send_mail(
        subject="Password Reset for {title}".format(title="TODO Application"),
        message=email_plaintext_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[reset_password_token.user.email]
    )
