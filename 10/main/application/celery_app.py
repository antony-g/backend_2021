import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')

app = Celery('main')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379'
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'count': {
        'task': 'main.tasks.count_users',
        'schedule': 6.0,
        # 'args': (,),
    },
}


if __name__ == '__main__':
    app.start()
