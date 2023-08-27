from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self) -> str:
        return reverse('blog:detail', kwargs={'pk': self.pk})
