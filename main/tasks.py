import logging
from celery import shared_task
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


@shared_task
def send_open_house_notification():
    try:
        logger.info('Starting send_open_house_notification task')
        send_mail(
            'День открытых дверей',
            'Уведомление о дне открытых дверей.',
            'your-email@example.com',
            ['recipient@example.com'],
            fail_silently=False,
        )
        logger.info('Email sent successfully')
        return 'Email sent successfully'
    except Exception as e:
        logger.error(f'Error sending email: {str(e)}')
        return str(e)
