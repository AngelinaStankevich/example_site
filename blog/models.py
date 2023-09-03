from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self) -> str:
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Post(title ={self.title}, id={self.id}, author_id={self.author_id})"
