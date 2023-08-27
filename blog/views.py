from django.views import generic
from django.utils import timezone
from .models import Post


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"


class PostCreateView(generic.CreateView):
    model = Post
    fields = ['title', 'body']


