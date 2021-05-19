from django.db import models
# from django.contrib.auth.models import User
from users.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    description = models.CharField(max_length=150, verbose_name='Описание задачи')
    due = models.DateField(verbose_name='Срок выполнения')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
