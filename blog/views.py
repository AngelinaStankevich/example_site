from django.views import generic
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django import shortcuts
from django.db import models

from .models import Post, Vote, Tag


def _vote(request, pk: int, up: bool):
    post = shortcuts.get_object_or_404(Post, pk=pk)
    Vote.objects.update_or_create(post=post, voter=request.user, defaults={'up': up})
    return shortcuts.redirect('blog:detail', pk=pk)


def upvote(request, pk: int):
    return _vote(request=request, pk=pk, up=True)


def downvote(request, pk: int):
    return _vote(request=request, pk=pk, up=False)


# IndexView - list of posts


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagListView(generic.ListView):
    template_name = "blog/tag_list.html"
    context_object_name = "tags"

    def get_queryset(self) -> models.QuerySet:
        return Tag.objects.order_by('title').all()


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = "blog/tag_detail.html"


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = ['title']