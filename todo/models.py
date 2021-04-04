from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todo')
    memo = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='todo/cover', blank=True)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.memo


class CheckList(models.Model):
    todo = models.ForeignKey(
        Todo, on_delete=models.CASCADE, related_name='checklist')
    text = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
