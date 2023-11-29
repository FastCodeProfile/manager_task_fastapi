import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery import Celery

from app.core.config import settings
from app.schemas.tasks import TaskScheme

celery = Celery(__name__, backend=settings.redis_dsn, broker=settings.redis_dsn,
                broker_connection_retry_on_startup=True)


@celery.task
def send_email(task: TaskScheme):
    msg = MIMEMultipart()
    msg['From'] = settings.EMAIL_FROM
    msg['To'] = settings.EMAIL_TO
    msg['Subject'] = "Новая задача с высоким приоритетом!"
    msg.attach(MIMEText(f"Задача №{task.id}\n\n"
                        f"Статус: {task.status}\n"
                        f"Приоритет: {task.priority}\n"
                        f"Название: {task.name}\n"
                        f"Описание: {task.description}\n"
                        , 'plain'))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
    return True
