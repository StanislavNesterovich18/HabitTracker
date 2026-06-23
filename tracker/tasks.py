from celery import shared_task

from tracker.services import send_telegram_message
from users.models import User


@shared_task
def send_tg_notification():
    message = "Не ленись, выполни привычку"
    for user in User.objects.filter(tg_id__isnull=False):
        if user.tg_id:
            send_telegram_message(user.tg_id, message)
        

