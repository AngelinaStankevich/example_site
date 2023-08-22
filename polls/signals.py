from django.db.models import signals
from . import models


def notify_users(sender: type[models.Question], instance: models.Question, created: bool, **kwargs):
    if created:
        # TODO : really notify all users
        print(f'Notify all users about new questions {instance.question_text!r}')


signal = signals.post_save.connect(receiver=notify_users, sender=models.Question)