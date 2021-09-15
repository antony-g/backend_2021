from __future__ import absolute_import

import os
from django.core.mail import send_mail
from celery import Celery, shared_task
from tornado import websocket


app = Celery('main', backend='redis://localhost', broker='pyamqp://')
os.environ['DJANGO_SETTINGS_MODULE'] = "application.settings"


# 1. Написать таск, который отправляет письмо админу при создании объекта в бд
@app.task
def send_email():
    send_mail(subject='Subject here',
              message='Here is the message.',
              from_email='from@example.com',
              recipient_list=['ks-garniz@rambler.ru'],
              fail_silently=False)


# 2. Написать периодический таск на какое-либо действие (например считать количество пользователей в системе каждые 5 мин и записывать в файл)
@shared_task
def count_users(request):
    users = request.user.get("???")
    return users


# 3. Использовать flower для мониторинга задач
# $ flower -A application --port=5555


# 4. Установить и поднять centrifugo, прикрутить к проекту, продемонстрировать отправку какого-то сообщения с помощью websocket
# $ docker pull centrifugo/centrifugo:v2.8.5

class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")
