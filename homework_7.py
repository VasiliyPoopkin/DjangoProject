import os
from django.conf import settings
from your_app.tasks import my_task
from celery import shared_task
from celery import Celery
from user.tasks import print_text
from .models import User, Purchase
from .tasks import print_purchase_count_task
from .models import User
from celery.schedules import crontab


#task 1

CELERY_BROKER_URL = 'redis://localhost:6379/0
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

app = Celery('Django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@shared_task
def my_task(arg1, arg2):
    result = arg1 + arg2
    return result

result = my_task.delay(10, 20)

#task 3

@shared_task
def print_text(text):
    print(text)

app = Celery('Django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

print_text.delay("Hello, Celery!")

#task 4

@shared_task
def print_purchase_count_task(user_id):
    try:
        user = User.objects.get(pk=user_id)
        purchase_count = Purchase.objects.filter(user=user).count()
        print(f"Purchase count for user {user_id}: {purchase_count}")
    except User.DoesNotExist:
        print(f"User with ID {user_id} does not exist.")

user_id_to_check = 114
print_purchase_count_task.delay(user_id_to_check)

#task 5

@shared_task
def print_user_count_task():
    user_count = User.objects.count()
    print(f"Total number of users in the database: {user_count}")

app = Celery('your_project')

app.conf.beat_schedule = {
    'print-user-count': {
        'task': 'user.tasks.print_user_count_task',
        'schedule': crontab(minute='*'),
    },
}