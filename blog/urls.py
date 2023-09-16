from django.urls import path

from . import views


app_name = "blog"  # namespace

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),  # polls:index
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.PostCreateView.as_view(), name="create_post"),
    path("<int:pk>/upvote", views.upvote, name="upvote"),
    path("<int:pk>/downvote", views.downvote, name="downvote"),
    path("tags/", views.TagListView.as_view(), name="tag_list"),
    path("tags/create", views.TagCreateView.as_view(), name="create_tag"),
    path("tags/<int:pk>", views.TagDetailView.as_view(), name="tag_detail"),
]
