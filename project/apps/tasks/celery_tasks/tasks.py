from django.core.mail import EmailMessage

from celery import shared_task

from tasks.models import Task
from users.models import User


@shared_task()
def send_task_is_done_email_task(user_id: int, task_id: int) -> None:
    try:
        user = User.objects.get(pk=user_id)
        task = Task.objects.get(pk=task_id)
    except (User.DoesNotExist, Task.DoesNotExist):
        return

    subject = f'TODO APP. Изменение в задаче с ID {task.id}'
    body = f'Задача "{task.title}" помечена выполненной'
    mail = EmailMessage(
        subject=subject,
        body=body,
        to=(user.email,)
    )
    mail.send()
