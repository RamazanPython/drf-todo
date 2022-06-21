from tasks.models import Task
from tasks.celery_tasks import send_task_is_done_email_task
from users.models import User


class TaskService:

    @staticmethod
    def mark_task_as_done(instance: Task,  user: User) -> Task:
        instance.is_done = True
        instance.save(update_fields=['is_done'])
        send_task_is_done_email_task.apply_async(
            kwargs={
                'user_id': user.pk,
                'task_id': instance.pk,
            }
        )
        return instance
