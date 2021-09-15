from django.db import models
from .tasks import send_email


class Object(models.Model):
    data = models.CharField(max_length=100, verbose_name='Данные')

    def save(self, *args, **kwargs):
        send_email()
        super(Object, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
