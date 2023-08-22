from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text: str = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


def notify_users(sender: type[Question], instance: Question, created: bool, **kwargs):
    if created:
        # TODO : really notify all users
        print(f'Notify all users about new questions {instance.question_text!r}')


signal = models.signals.post_save.connect(receiver=notify_users, sender=Question)
