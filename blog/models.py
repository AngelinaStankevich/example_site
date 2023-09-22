from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ) -> None:
        self.title = self.title.lower()
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def get_absolute_url(self) -> str:
        return reverse('blog:tag_detail', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(to=Tag, related_name='posts')
    pub_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['title', 'author']

    def get_absolute_url(self) -> str:
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Post(title ={self.title}, id={self.id}, author_id={self.author_id})"

    @property
    def rating(self) -> int:
        return self.upvotes - self.downvotes

    @property
    def upvotes(self) -> int:
        return len(self.vote_set.filter(up=True))

    @property
    def downvotes(self) -> int:
        return len(self.vote_set.filter(up=False))


class Vote(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    voter = models.ForeignKey(to=User, on_delete=models.CASCADE)
    up = models.BooleanField(null=False)

    class Meta:
        unique_together = ('post', 'voter')

