from rest_framework import viewsets, filters, pagination

from . import serializers, models


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class PostPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    pagination_class = PostPagination

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'id', 'body']
    search_fields = ['title']


class VoteViewSet(viewsets.ModelViewSet):
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer





