from django.conf import settings
from django.core.mail import send_mail

from mail_notifications.celery import app as celery_app


@celery_app.task
def send_notification_task(subject, message, recipients):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipients,
        fail_silently=False,
    )
